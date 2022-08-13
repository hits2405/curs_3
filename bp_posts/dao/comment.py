class Comment:
    """
    Чтение данных для использования
    """

    def __init__(self,
                 pk,
                 commenter_name,
                 comment,
                 post_id
                 ):
        """
        Инициализация переменных из json
        """
        self.pk = pk
        self.post_pk = post_id
        self.commenter_name = commenter_name
        self.comment = comment

    def __repr__(self):
        """
        Возврат данных для работы с ними
        """
        return f"Comment( " \
               f"{self.pk}," \
               f"{self.post_pk}," \
               f"{self.commenter_name}," \
               f"{self.comment}" \
               f")"

