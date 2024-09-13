from final_model import load_data, perform_one_hot_encoding, train_test_split

dataset = load_data()


def test_data_loading():
    assert not dataset.empty


def test_columns_existance():
    assert "Year" in dataset.columns
    assert "Total crimes" in dataset.columns
    assert "Total Nuisance Next Year" in dataset.columns
    assert "Unemployment" in dataset.columns
    assert "Population" in dataset.columns
    assert "Neighbourhood" in dataset.columns


def test_one_hot_encoding():
    df_encoded = perform_one_hot_encoding(dataset)

    assert "Neighbourhood" not in df_encoded.columns
    assert len(df_encoded.columns) == 61


def test_train_test_split():
    df_encoded = perform_one_hot_encoding(dataset)
    X_train, X_test, y_train, y_test = train_test_split(df_encoded)

    assert len(X_train.columns) == 59
    assert len(X_test.columns) == 59
