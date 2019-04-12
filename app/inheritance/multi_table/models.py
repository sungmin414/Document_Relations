from django.db import models


class Place1(models.Model):
    # 암시적으로 생성되는 PK Field
    # id = models.AutoField(Primary_key=True)
    # -> 임의의 필드에 primary_key=True 옵션을 주면 id 필드가 생성되지 않음
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return f'{self.name} [Place]'

    class Meta:
        db_table = 'Inheritance_MultiTable_Place'


def get_removed_place():
    # 밑에 내용줄여서 쓰면 return Place1.objects.get_or_create(name='철거됨')[0]
    try:
        place = Place1.objects.get(name='철거됨')
    except Place1.DoesNotExist:
        place = Place1.objects.create(name='철거됨')
    return place


class Restaurant1(Place1):
    # MultiTable inheritance구현 시 암시적으로 생성되는 OTO Field
    # <부모클래스의 소문자화>_ptr = models.OneToOneField(<부모클래스>)
    # PLace1_ptr = models.OneToOneField(Place1, primary_key=True)
    #   -> 임의의 필드에 parent_link=True 옵션을 주면 <부모클래스의 소문자화>_ptr 필드가 생성되지 않음
    place_ptr = models.OneToOneField(
        Place1,
        on_delete=models.CASCADE,
        parent_link=True,
        primary_key=True,
    )

    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    # OTO으로 구현할 내용 아님
    old_place = models.ForeignKey(
        Place1, verbose_name='이전에 가게가 있던 장소',
        # 만약에 이전에 가게가 있던 건물이 없어질 경우
        # (해당 장소 또는 건물이 없어졌음) 이라는 정보를 담자
        # -> 위와 같은 정보를 담고 있는 Place1객체 (DB row)가 필요함
        on_delete=models.SET(get_removed_place),
        # Place목록 중에서, 자신이 old_place인 경우에 해당하는 Restaurant목록
        # -> 즉, 자신(장소)에 있었던 Restaurant목록 -> (그 장소에) 예전에 있던 식당 목록
        related_name='old_restaurants',
        related_query_name='old_restaurant',
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.name} [Restaurant]'

    class Meta:
        db_table = 'Inheritance_MultiTable_Restaurant'

