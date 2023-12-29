import mysql.connector
def get_factor_value(factor_id):
    # 连接到 MySQL 数据库，替换为你的实际数据库连接信息
    db_connection = mysql.connector.connect(
        host="192.168.200.182",
        user="smartuser",
        password="!QAZ2wsx#EDC",
        port='63306',
        database='application'
    )

    # 创建游标对象
    cursor = db_connection.cursor(buffered=True)

    try:
        # 执行查询
        query = f"SELECT factor_value FROM ads_index_factor_newest_period WHERE factor_id = {factor_id} and subject_code = '930903.CSI'"
        cursor.execute(query)

        # 获取查询结果
        result = cursor.fetchone()
        return result[0] if result else None

    finally:
        # 关闭游标和数据库连接
        cursor.close()
        db_connection.close()

def generate_text_149800000008():
    # 获取因子值
    p1 = get_factor_value(149800000008)

    # 生成目标文本
    if p1 == 1:
        return '创历史新高'
    elif p1 == -1:
        return '创历史新低'
    else:
        return ''


def generate_text_411000000001():
    # 获取因子值
    p2 = get_factor_value(411000000001)

    # 生成目标文本
    if p2 > 0:
        return f'连续{p2}周/月/期 及以上上升'
    elif p2 < 0:
        return f'连续{abs(p2)}周/月/期 及以上下降'
    else:
        return ''

def generate_text_12800000097():
    # 获取因子值
    p2 = get_factor_value(12800000097)

    # 生成目标文本
    if p2 > 0:
        return f'连续{p2}周/月/期 及以上上升'
    elif p2 < 0:
        return f'连续{abs(p2)}周/月/期 及以上下降'
    else:
        return ''


def generate_text_149800000014():
    # 获取因子值
    p3 = get_factor_value(149800000014)

    # 生成目标文本
    if p3 > 0.8:
        return f'处{p3*100:.2f}%历史高位'
    elif p3 < 0.2:
        return f'处{p3*100:.2f}%历史低位'
    else:
        return ''

def generate_text_149800000015():
    # 获取因子值
    p3 = get_factor_value(149800000015)

    # 生成目标文本
    if p3 > 0.8:
        return f'处{p3*100:.2f}%历史高位'
    elif p3 < 0.2:
        return f'处{p3*100:.2f}%历史低位'
    else:
        return ''

indicator_name1 = ['EPS(单季度)同比增速']
indicator_name2 = ['EPS(TTM)同比增速']
indicator_name3 = ['营业总收入(单季度)同比增速']

indicator_name1 = ['EPS成长评分','收入回报评分','财务健康评分']

def generate_market_eps_yoy_text():
    for indicator in indicator_name1:
        text = indicator + ":"
        text += generate_text_149800000008()
        text += generate_text_411000000001()
        text += generate_text_149800000014()
    return text

def generate_market_eps_ttm_text():
    for indicator in indicator_name2:
        text = indicator
        text += generate_text_149800000015()
    return text
def generate_market_total_income_text():
    for indicator in indicator_name3:
        text = indicator
        text += generate_text_12800000097()
    return text



text1 = generate_market_eps_yoy_text()
text2 = generate_market_eps_ttm_text()
text3 = generate_market_total_income_text()

print("财务：" + text1, text2, text3, sep=";")