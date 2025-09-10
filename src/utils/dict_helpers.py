from utils.custom_exception import CustomException


def certain_get[K, V](item: dict[K, V], key: K) -> V:
    value = item.get(key)

    if value is not None:
        return value

    raise CustomException(f"{__name__}: key:{key}")
