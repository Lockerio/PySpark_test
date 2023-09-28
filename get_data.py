def get_joined_dataframes(product_df, category_df, product_category_df):
    result_df = product_df.join(product_category_df, product_category_df["id_product"] == product_df["id"], "left")\
        .join(category_df, product_category_df["id_category"] == category_df["id"], "left")\
        .select(product_df["name"].alias("Product"), category_df["name"].alias("Category"))
    return result_df
