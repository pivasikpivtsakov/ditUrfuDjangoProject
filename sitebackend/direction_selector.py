from sitebackend.models import DirectionGroup


def select_directions(codes: list[str]) -> None:
    """
    принимает выбранные галочки, selected=1 для выбранных, selected=0 для невыбранных (не переданных в codes)
    я бы выбрал другой формат передачи данных
    задаем для каждого направления гуид в базе
    передаем вместе с набором направлений на клиент
    там выбираются галочки
    нам на сервер направляются гуиды выбранных и мы можем куда проще сделать запрос в базу
    но реализовать способ из тестового было даже весело
    :param codes: ['4444.44', '1212.12']
    """
    # сделаем словарь {группа: направление, группа: направление...}
    splitted_codes = [i.split('.') for i in codes]
    codes_dict = dict()
    for splitcode in splitted_codes:
        key:str = splitcode[0]
        value:str = splitcode[1]
        if key not in codes_dict.keys():
            codes_dict[key] = [value]
        else:
            codes_dict[key].append(value)
    # запишем отмеченные и неотмеченные в базу в поле selected
    checked_groups = DirectionGroup.objects.filter(code__in=codes_dict.keys())
    unchecked_groups = DirectionGroup.objects.exclude(code__in=codes_dict.keys())
    for g in checked_groups:
        g.directions.filter(code__in=codes_dict[str(g.code)]).update(selected=True)
        g.directions.exclude(code__in=codes_dict[str(g.code)]).update(selected=False)
        g.save()
    for g in unchecked_groups:
        g.directions.update(selected=False)
        g.save()
