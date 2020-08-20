import pandas as pd


def get_avg(df, categories, types):
    """ This function creates a column for each category, called `{category}_avg` where the value is the percentage of
    annotators that put this category in a given bio! It does the same for each type of account."""

    for category in categories:
        df[category + "_avg"] = df.apply(lambda x: (int(category in x["coarsecat1"]) +
                                                    int(category in x["coarsecat2"]) +
                                                    int(category in x["coarsecat3"]) +
                                                    int(category in x["coarsecat4"])) /
                                                   sum([x["coarsecat1"] != "",
                                                        x["coarsecat2"] != "",
                                                        x["coarsecat3"] != "",
                                                        x["coarsecat4"] != ""]), axis=1)
    for typ in types:
        df[typ + "_avg"] = df.apply(lambda x: (int(typ in x["type1"]) +
                                               int(typ in x["type2"]) +
                                               int(typ in x["type3"]) +
                                               int(typ in x["type4"])) /
                                              sum([x["category1"] != "",
                                                   x["category2"] != "",
                                                   x["category3"] != "",
                                                   x["category4"] != ""]), axis=1)

    return df


def matching_dataframe_categorical(df_before, df_matched, treat_var, categorical_var):
    helper_input = [(df_matched, 0, "Control", "Matched"),
                    (df_matched, 1, "Treated", "Matched"),
                    (df_before, 0, "Control", "Source"),
                    (df_before, 1, "Treated", "Source")]

    helper_output = []
    for df, treat, group_flag, kind_flag in helper_input:
        tmp = pd.get_dummies(df[df[treat_var] == treat][categorical_var]).mean(axis=0)
        tmp = pd.DataFrame([tmp,
                            pd.Series([group_flag] * len(tmp), index=tmp.index),
                            pd.Series([kind_flag] * len(tmp), index=tmp.index)],
                           index=["val", "group", "kind"]).T.reset_index()
        helper_output.append(tmp)
    df_cats = pd.concat(helper_output, axis=0)
    return df_cats
