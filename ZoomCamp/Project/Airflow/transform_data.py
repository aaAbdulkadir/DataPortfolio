def pyspark_transformations(api_filepath, bs4_filepath, airflow_home):

    from pyspark.sql import SparkSession
    import pandas as pd

    print('Building spark session...')

    spark = SparkSession.builder \
    .master("local[*]") \
    .appName('project').getOrCreate()

    df = spark.read.parquet(api_filepath, header=True, inferSchema=True)

    # partition the data
    df = df.repartition(24)

    # save partitioned file
    df.write.parquet(airflow_home + '/output/partitioned/', mode='overwrite')

    # read partitioned data in
    api_df = spark.read.parquet(airflow_home + '/output/partitioned/*', header=True, inferSchema=True)

    # transformations
    top_ranked = api_df[['symbol', 'name', 'market_cap']].orderBy('cmc_rank', ascending=True)

    top_ranked_fluctuations = api_df[['name', 'percent_change_1h', 'percent_change_24h', 'percent_change_7d', 'percent_change_30d', 'percent_change_60d', 'percent_change_90d']] \
    .orderBy('cmc_rank', ascending=True)

    best_performing_90_days = api_df[['symbol', 'name', 'price', 'percent_change_90d']] \
    .filter('market_cap > 1000000000').orderBy('percent_change_90d', ascending=False)

    price_chart = api_df[['last_updated', 'symbol', 'name', 'price']].orderBy('cmc_rank', ascending=True)

    top_gainers = api_df[['symbol', 'name', 'percent_change_24h']] \
    .filter('volume_24h > 50000 and cmc_rank < 100').orderBy('percent_change_24h', ascending=False)

    top_losers = api_df[['symbol', 'name', 'percent_change_24h']] \
    .filter('volume_24h > 50000 and cmc_rank < 100').orderBy('percent_change_24h', ascending=True)

    # stacked column chart for price changes
    top_ranked_fluctuations = top_ranked_fluctuations.toPandas()
    top_ranked_fluctuations = top_ranked_fluctuations.set_index('name')
    top_ranked_fluctuations = top_ranked_fluctuations.stack().to_frame(name='values')
    top_ranked_fluctuations = top_ranked_fluctuations.rename(columns={'level_1':'Time Frame', 'values':'Percentage Change'})
    top_ranked_fluctuations['Time Frame'] = top_ranked_fluctuations['Time Frame'].str.replace('percent_change_', '', regex=False)

    # change bs4 data to csv
    bs4_df = spark.read.parquet(bs4_filepath, header=True, inferSchema=True)

    top_ranked.toPandas().to_csv(airflow_home + '/output/top_ranked.csv')
    top_ranked_fluctuations.to_csv(airflow_home + '/output/top_ranked_fluctuations.csv')
    best_performing_90_days.toPandas().to_csv(airflow_home + '/output/best_performing_90_days.csv')
    price_chart.toPandas().to_csv(airflow_home + '/output/price_chart.csv')
    top_gainers.toPandas().to_csv(airflow_home + '/output/top_gainers.csv')
    top_losers.toPandas().to_csv(airflow_home + '/output/top_losers.csv')
    bs4_df.toPandas().to_csv(airflow_home + '/output/bs4_df.csv')
