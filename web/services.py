def filter_news(tag, news_qs, filters: dict):
    if filters.__contains__('search'):
        news_qs = news_qs.filter(title__icontains=filters["search"]) \
                  | news_qs.filter(text__icontains=filters["search"])

    if filters.__contains__('sort'):
        news_qs = news_qs.order_by(filters["sort"])

    if filters.__contains__('category'):
        news_qs = news_qs.filter(tags__title__in=['test1'])

    return news_qs
