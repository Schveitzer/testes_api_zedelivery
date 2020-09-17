class ObjectHelper:  # pylint: disable=too-few-public-methods

    @staticmethod
    def remove_keys(obj, keys_to_remove):
        for key in list(obj.keys()):  # Use a list instead of a view
            if key in keys_to_remove:
                del obj[key]  # Delete a key from obj
        return obj
