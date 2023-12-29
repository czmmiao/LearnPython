"""
担任python开发专家，根据需求编写函数。
***仅编写python代码，添加函数内部的中文注释***
****特别注意，不要包含其他任何信息，不要包含示例用法***

需求：

1. 函数名徐遵循：{PRD_REQUEST}_{Indicator_name}_{Indicator_id1}_{Indicator_id2}的命名方式

2. 该函数不要传入任何参数

3. p_value = get_factor_value({Indicator_id}), Indicator_id可能包含多个，需逐一取值。需用实际Indicator_id的替代

4. if p_value = None then return ''

5. 逻辑：
PRD_REQUEST	Indicator_name	indicator_id	Comment	Logic
MarketTrendFinance	EPS_YOY	p2=149800000014 	指数.EPS(单季度)同比	"if p2=1 then 创历史新高
p2 =-1 then 创历史新低"


"""




import mysql.connector

def get_factor_value(factor_id):
    # 连接到 MySQL 数据库，替换为你的实际数据库连接信息
    # db_connection = mysql.connector.connect(
    #     host="192.168.200.182",
    #     user="smartuser",
    #     password="!QAZ2wsx#EDC",
    #     port='63306',
    #     database='application'
    # )

    db_connection = mysql.connector.connect(
        host="192.168.200.149",
        user="smartuser",
        password="!QAZ2wsx#EDC",
        port='13306',
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

def MarketTrendFinance_EPS_YOY_149800000008():
    """
    指数.EPS(单期度)同比

    该函数用于根据指数.EPS(单期度)同比趋势，生成相应的目标文本。

    参数:
        无

    返回:
        str: 生成的目标文本，可能为 '创历史新高' 或 '创历史新低'

    注释:
        - 通过 get_factor_value(149800000008) 获取因子值 p1。
        - 当 p1 == 1 时，返回 '创历史新高'。
        - 当 p1 == -1 时，返回 '创历史新低'。
        - 如果 p1 为其他值，则返回空字符串。

    示例调用:
        result = MarketTrendFinance_EPS_YOY_149800000008()
        print(result)
    """
    # 获取因子值
    p1 = get_factor_value(149800000008)

    # 生成目标文本
    if p1 == 1:
        return '创历史新高'
    elif p1 == -1:
        return '创历史新低'
    else:
        return ''


def MarketTrendFinance_EPS_YOY_411000000001():
    """
    根据EPS同比趋势判断指标值计算评分。

    返回:
    str: 根据给定逻辑的评分变化。
    """
    # 获取EPS同比趋势判断指标值
    p_value = get_factor_value(411000000001)

    # 检查是否为None值
    if p_value is None:
        return ''

    # 定义参数
    p2 = p_value

    # 评估逻辑
    if p2 > 3:
        return f'连续{abs(int(p2))}期上升'
    elif p2 < -3:
        return f'连续{int(abs(p2))}期下降'
    else:
        return ''


def MarketTrendFinance_EPS_YOY_149800000014():
    """
    根据EPS同比指标值判断历史新高或新低。

    返回:
    str: 根据给定逻辑的历史新高或新低。
    """
    # 获取EPS同比指标值
    p_value = get_factor_value(149800000014)

    # 检查是否为None值
    if p_value is None:
        return ''

    # 定义参数
    p2 = p_value

    # 评估逻辑
    if p2 == 1:
        return '创历史新高'
    elif p2 == -1:
        return '创历史新低'
    else:
        return ''


def MarketTrendFinance_EPS_TTM_149800000010():
    """
    指数.EPS(TTM)同比_趋势判断

    该函数用于根据指数.EPS(TTM)同比趋势，生成相应的目标文本。

    参数:
        无

    返回:
        str: 生成的目标文本，可能为 '创历史新高' 或 '创历史新低'

    注释:
        - 通过 get_factor_value(149800000010) 获取因子值 p1。
        - 当 p1 == 1 时，返回 '创历史新高'。
        - 当 p1 == -2 时，返回 '创历史新低'。
        - 如果 p1 为其他值，则返回空字符串。

    示例调用:
        result = MarketTrendFinance_EPS_TTM_149800000010()
        print(result)
    """
    # 获取因子值
    p1 = get_factor_value(149800000010)

    # 生成目标文本
    result = '创历史新高' if p1 == 1 else '创历史新低' if p1 == -2 else ''

    return result


def MarketTrendFinance_TotalEarning_YOY_412300000001():
    """
    根据营业总收入同比指标值计算期度趋势。

    返回:
    str: 根据给定逻辑的期度趋势变化。
    """
    # 获取营业总收入同比指标值
    p_value = get_factor_value(412300000001)

    # 检查是否为None值
    if p_value is None:
        return ''

    # 定义参数
    p2 = p_value

    # 评估逻辑
    if p2 > 3:
        return f'连续{abs(int(p2))}期上升'
    elif p2 < -3:
        return f'连续{int(abs(p2))}期下降'
    else:
        return ''

def MarketTrendFinance_EPS_RATING_521700000006_521700000007():
    """
    指数.EPS评分函数

    Returns:
    - str: 返回EPS评分结果，如果 p2>0.05 则返回 math.ceil(p1) 分，如果 p2<-0.05 则返回 math.ceil(p1) 分，否则返回空字符串
    """
    # 逐一取得指标值
    p1 = get_factor_value(521700000006)
    p2 = get_factor_value(521700000007)

    # 检查 p_value 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评分计算
    if p2 > 0.05:
        return '上升' + str(math.ceil(p1)) + '分'  # 向上取整
    elif p2 < -0.05:
        return '下降' + str(math.ceil(p1)) + '分'  # 向上取整
    else:
        return ''  # 其他情况返回空字符串

import math

def MarketTrendFinance_EARNING_RATING_522500000003_522500000004():
    """
    指数.收入回报评分函数

    Returns:
    - str: 返回收入回报评分结果，如果 p2>0.05 则返回 math.ceil(p1) 分，如果 p2<-0.05 则返回 math.ceil(p1) 分，否则返回空字符串
    """
    # 逐一取得指标值
    p1 = get_factor_value(522500000003)
    p2 = get_factor_value(522500000004)

    # 检查 p_value 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评分计算
    if p2 > 0.05:
        return '上升' + str(math.ceil(p1)) + '分'  # 向上取整
    elif p2 < -0.05:
        return '下降' + str(math.ceil(p1)) + '分'  # 向上取整
    else:
        return ''  # 其他情况返回空字符串



def MarketTrendFinance_REPORTING_RATING_522600000004_522600000001():
    """
    根据财报健康评分指标值计算评分。

    返回:
    str: 根据给定逻辑的评分变化。
    """
    # 获取P1和P2的值
    p1_value = get_factor_value(522600000004)
    p2_value = get_factor_value(522600000001)

    # 检查P1和P2是否为None值
    if p1_value is None or p2_value is None:
        return ''

    # 定义P1和P2参数
    p1 = p1_value
    p2 = p2_value

    # 评估逻辑
    if p2 > 0.05:
        return f'上升{p1}分'
    elif p2 < -0.05:
        return f'下降{p1}分'
    else:
        return ''


def MarketTrendFinaceText():
    EPS_YOY_TEXT = ""
    EPS_YOY_TEXT += MarketTrendFinance_EPS_YOY_411000000001()
    EPS_YOY_TEXT += MarketTrendFinance_EPS_YOY_149800000008()
    EPS_YOY_TEXT += MarketTrendFinance_EPS_YOY_149800000014()

    EPS_TTM = ""
    EPS_TTM += MarketTrendFinance_EPS_TTM_149800000010()

    TOTAL_EARNING = ""
    TOTAL_EARNING += MarketTrendFinance_TotalEarning_YOY_412300000001()

    EPS_RATING = ""
    EPS_RATING += MarketTrendFinance_EPS_RATING_521700000006_521700000007()


    REPORT_RATING = ""
    REPORT_RATING += MarketTrendFinance_REPORTING_RATING_522600000004_522600000001()

    EARNING_RATING = ""
    EARNING_RATING += MarketTrendFinance_EARNING_RATING_522500000003_522500000004()

    result_text = "财务："

    if EPS_YOY_TEXT:
        result_text += "EPS(单季度)同比增速" + EPS_YOY_TEXT + "；"

    if EPS_TTM:
        result_text += "EPS(TTM)同比增速" + EPS_TTM + "；"

    if TOTAL_EARNING:
        result_text += "营业总收入(单季度)同比增速" + TOTAL_EARNING + "；"

    if EPS_RATING:
        result_text += "EPS评分" + EPS_RATING + "；"

    if REPORT_RATING:
        result_text += "财务健康评分" + REPORT_RATING + "；"

    if EARNING_RATING:
        result_text += "收入回报评分" + EARNING_RATING + "；"

    if result_text == "财务：":
        result_text = ''
    else:
        result_text = result_text[:-1] + "。"

    return result_text
def MarketTrendExpect_Expect_Ratio_240300000009_240300000007():
    """
    预告净利润超预期个股占比函数

    Returns:
    - str: 如果 p1=1 则返回"预告净利润超预期个股占比{p2}%,创历史新高"，如果 p1=-1 则返回"预告净利润超预期个股占比{p2}%,创历史新低"，否则返回空字符串
    """
    # 获取指标值
    p1 = get_factor_value(240300000009)
    p2 = get_factor_value(240300000007)

    # 检查 p_value 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行判断
    if p1 == 1:
        return f'预告净利润超预期个股占比为{round(p2*100, 2)}%，创历史新高'
    elif p1 == -1:
        return f'预告净利润超预期个股占比为{round(p2*100, 2)}%，创历史新低'
    else:
        return ''  # 其他情况返回空字符串


def MarketTrendExpect_Expect_Ratio_411300000001():
    """
    指数.EPS(单期度)同比_趋势判断函数

    Returns:
    - str: 如果 p2>3 则返回"连续int(p2)期上升"，如果 p2<-3 则返回"连续int(p2)期下降"，否则返回空字符串
    """
    # 获取指标值
    p2 = get_factor_value(411300000001)

    # 检查 p_value 是否为 None
    if p2 is None:
        return ''

    # 根据逻辑进行判断
    if p2 > 3:
        return f'连续{abs(int(p2))}期上升'
    elif p2 < -3:
        return f'连续{abs(int(p2))}期下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendExpect_Expect_Ratio_191000000025():
    """
    指数.EPS(单期度)同比_趋势判断函数

    Returns:
    - str: 如果 p2>3 则返回"连续int(p2)周上升"，如果 p2<-3 则返回"连续int(p2)周下降"，否则返回空字符串
    """
    # 获取指标值
    p2 = get_factor_value(191000000025)

    # 检查 p_value 是否为 None
    if p2 is None:
        return ''

    # 根据逻辑进行判断
    if p2 > 3:
        return f'连续{abs(int(p2))}周上升'
    elif p2 < -3:
        return f'连续{abs(int(p2))}周下降'
    else:
        return ''  # 其他情况返回空字符串



def MarketTrendExpectText():
    EXPECT_RATIO_TEXT1 = ""
    EXPECT_RATIO_TEXT1 += MarketTrendExpect_Expect_Ratio_240300000009_240300000007()
    EXPECT_RATIO_TEXT1 += MarketTrendExpect_Expect_Ratio_411300000001()

    EXPECT_RATIO_TEXT2 = ""
    EXPECT_RATIO_TEXT2 += MarketTrendExpect_Expect_Ratio_191000000025()

    result_text = "业绩预期："
    if EXPECT_RATIO_TEXT1:
        result_text += "9M23" + EXPECT_RATIO_TEXT1 + "；"

    if EXPECT_RATIO_TEXT2:
        result_text += "一致预期净利润同比增速（2023E)" + EXPECT_RATIO_TEXT2 + "；"

    if result_text == "业绩预期：":
        result_text = ''
    else:
        result_text = result_text[:-1] + "。"

    return result_text

x1 = MarketTrendFinaceText()
print(x1)
x2 = MarketTrendExpectText()
print(x2)



def MarketTrendEvaluation_PETTM_418700000002():
    """
    指数.PE(TTM)历史分位评估函数

    Returns:
    - str: 如果 p>0.8 则返回"处{p}%历史高位"，如果 p<0.2 则返回"处{p}%历史低位"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(418700000002)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 0.8:
        return f'PE(TTM)处{round(p*100,2)}%历史高位'
    elif p < 0.2:
        return f'PE(TTM)处{round(p*100,2)}%历史低位'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendEvaluation_PETTM_176800000007():
    """
    指数.PE(TTM)边际趋势(周)评估函数

    Returns:
    - str: 如果 p>3 则返回"连续int(p)周上升"，如果 p<-3 则返回"连续int(p)周下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(176800000007)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}周上升'
    elif p < -3:
        return f'连续{abs(int(p))}周下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendEvaluation_PBTTM_418800000002():
    """
    指数.PB(TTM)历史分位评估函数

    Returns:
    - str: 如果 p>0.8 则返回"处{p}%历史高位"，如果 p<0.2 则返回"处{p}%历史低位"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(418800000002)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 0.8:
        return f'处{round(p*100,2)}%历史高位'
    elif p < 0.2:
        return f'处{round(p*100,2)}%历史低位'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendEvaluation_PBTTM_177200000006():
    """
    指数.PB(TTM)边际趋势(周)评估函数

    Returns:
    - str: 如果 p>3 则返回"连续int(p)周上升"，如果 p<-3 则返回"连续int(p)周下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(177200000006)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}周上升'
    elif p < -3:
        return f'连续{abs(int(p))}周下降'
    else:
        return ''  # 其他情况返回空字符串
def MarketTrendEvaluation_PEGTTM_176900000004():
    """
    指数.PEG(TTM)截面分位评估函数

    Returns:
    - str: 如果 p>0.8 则返回"全市场分位处{p}%高位"，如果 p<0.2 则返回"处{p}%市场低位"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(176900000004)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 0.8:
        return f'全市场分位处{round(p*100,2)}%高位'
    elif p < 0.2:
        return f'处{round(p*100,2)}%市场低位'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendEvaluation_PEGTTM_176900000005():
    """
    指数.PEG(TTM)边际趋势(周)评估函数

    Returns:
    - str: 如果 p>3 则返回"连续int(p)周上升"，如果 p<-3 则返回"连续int(p)周下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(176900000005)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}周上升'
    elif p < -3:
        return f'连续{abs(int(p))}周下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendEvaluation_DIVIDEND_TTM_177800000001():
    """
    指数.股息率(TTM)截面分位评估函数

    Returns:
    - str: 如果 p>0.8 则返回"全市场分位处{p}%高位"，如果 p<0.2 则返回"处{p}%市场低位"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(177800000001)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 0.8:
        return f'全市场分位处{round(p*100,2)}%高位'
    elif p < 0.2:
        return f'处{round(p*100,2)}%市场低位'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendEvaluation_DIVIDEND_TTM_177800000002():
    """
    指数.股息率(TTM)边际趋势(周)评估函数

    Returns:
    - str: 如果 p>3 则返回"连续int(p)周上升"，如果 p<-3 则返回"连续int(p)周下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(177800000002)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}周上升'
    elif p < -3:
        return f'连续{abs(int(p))}周下降'
    else:
        return ''  # 其他情况返回空字符串

import math

def MarketTrendEvaluation_EVALTION_RATING_538300000002_538300000004():
    """
    指数.EPS评分函数

    Returns:
    - str: 返回EPS评分结果，如果 p2>0.05 则返回 math.ceil(p1) 分，如果 p2<-0.05 则返回 math.ceil(p1) 分，否则返回空字符串
    """
    # 逐一取得指标值
    p1 = get_factor_value(538300000002)
    p2 = get_factor_value(538300000004)

    # 检查 p_value 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评分计算
    if p2 > 0.05:
        return str(math.ceil(p1)) + '分'  # 向上取整
    elif p2 < -0.05:
        return str(math.ceil(p1)) + '分'  # 向上取整
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendEvaluation_EVALTION_RATING_538300000003():
    """
    指数.估值评分(期)边际趋势函数

    Returns:
    - str: 如果 p>3 则返回"连续int(p)期上升"，如果 p<-3 则返回"连续int(p)期下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(538300000003)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}期上升'
    elif p < -3:
        return f'连续{abs(int(p))}期下降'
    else:
        return ''  # 其他情况返回空字符串



def MarketTrendEvaluationText():
    EVALUATION_PETTM_TEXT = ""
    EVALUATION_PETTM_TEXT += MarketTrendEvaluation_PETTM_176800000007()
    EVALUATION_PETTM_TEXT += MarketTrendEvaluation_PETTM_418700000002()

    EVALUATION_PBTTM_TEXT = ""
    EVALUATION_PBTTM_TEXT += MarketTrendEvaluation_PBTTM_418800000002()
    EVALUATION_PBTTM_TEXT += MarketTrendEvaluation_PBTTM_177200000006()

    EVALUTION_PEGTTM_TEXT = ""
    EVALUTION_PEGTTM_TEXT += MarketTrendEvaluation_PEGTTM_176900000004()
    EVALUTION_PEGTTM_TEXT += MarketTrendEvaluation_PEGTTM_176900000005()

    EVALUTION_PEGTTM_TEXT = ""
    EVALUTION_PEGTTM_TEXT += MarketTrendEvaluation_PEGTTM_176900000004()
    EVALUTION_PEGTTM_TEXT += MarketTrendEvaluation_PEGTTM_176900000005()

    EVALUATION_DIVIDEND_TEXT = ""
    EVALUATION_DIVIDEND_TEXT += MarketTrendEvaluation_DIVIDEND_TTM_177800000001()
    EVALUATION_DIVIDEND_TEXT += MarketTrendEvaluation_DIVIDEND_TTM_177800000002()

    EVALUATION_RATING_TEXT = ""
    EVALUATION_RATING_TEXT += MarketTrendEvaluation_EVALTION_RATING_538300000002_538300000004()
    EVALUATION_RATING_TEXT += MarketTrendEvaluation_EVALTION_RATING_538300000003()


    result_text = "估值："
    if EVALUATION_PETTM_TEXT:
        result_text += EVALUATION_PETTM_TEXT + "；"

    if EVALUATION_PBTTM_TEXT:
        result_text += "PB(MRQ)" + EVALUATION_PBTTM_TEXT + "；"

    if EVALUTION_PEGTTM_TEXT:
        result_text += EVALUTION_PEGTTM_TEXT + "；"

    if EVALUATION_DIVIDEND_TEXT:
        result_text += EVALUATION_DIVIDEND_TEXT + "；"

    if EVALUATION_RATING_TEXT:
        result_text += EVALUATION_RATING_TEXT + "；"

    if result_text == "估值：":
        result_text = ''
    else:
        result_text = result_text[:-1] + "。"

    return result_text

x3 = MarketTrendEvaluationText()
print(x3)

def MarketTrendFund_FUND_RATIO_416800000002():
    """
    指数.主动偏股型基金持仓占比历史分位函数

    Returns:
    - str: 如果 p>0.8 则返回"处{p}%历史高位"，如果 p<0.2 则返回"处{p}%历史高位"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(416800000002)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 0.8:
        return f'处{round(p*100,2)}%历史高位'
    elif p < 0.2:
        return f'处{round(p*100,2)}%历史高位'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendFund_FUND_RATIO_416800000001():
    """
    指数.主动偏股型基金持仓占比边际趋势函数

    Returns:
    - str: 如果 p>3 则返回"连续int(p)期上升"，如果 p<-3 则返回"连续int(p)期下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(416800000001)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}期上升'
    elif p < -3:
        return f'连续{abs(int(p))}期下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendFund_LGT_RATIO_417300000002():
    """
    指数.陆股通持股比例历史分位函数

    Returns:
    - str: 如果 p>0.8 则返回"处{p}%历史高位"，如果 p<0.2 则返回"处{p}%历史高位"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(417300000002)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 0.8:
        return f'处{round(p*100,2)}%历史高位'
    elif p < 0.2:
        return f'处{round(p*100,2)}%历史高位'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendFund_LGT_RATIO_417300000003():
    """
    指数.陆股通持股比例边际趋势(周)函数

    Returns:
    - str: 如果 p>3 则返回"连续int(p)期上升"，如果 p<-3 则返回"连续int(p)期下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(417300000003)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}期上升'
    elif p < -3:
        return f'连续{abs(int(p))}期下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendFund_MANAGEMENT_RATIO_240800000021_417700000003():
    """
    指数.近1月管理层增持比例函数

    Returns:
    - str: 如果 p2>3 则返回"{p1}%,连续int(p2)周上升"，如果 p2<-3 则返回"{p1}%,连续int(p2)周下降"，否则返回空字符串
    """
    # 逐一取得指标值
    p1 = get_factor_value(240800000021)
    p2 = get_factor_value(417700000003)

    # 检查 p_value 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评估
    if p2 > 3:
        return f'{p1}%,连续{abs(int(p2))}周上升'
    elif p2 < -3:
        return f'{p1}%,连续{abs(int(p2))}周下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendFund_BUYBACK_RATIO_240800000022_417800000003():
    """
    指数.近1月回购比例函数

    Returns:
    - str: 如果 p2>3 则返回"{p1}%,连续int(p2)周上升"，如果 p2<-3 则返回"{p1}%,连续int(p2)周下降"，否则返回空字符串
    """
    # 逐一取得指标值
    p1 = get_factor_value(240800000022)
    p2 = get_factor_value(417800000003)

    # 检查 p_value 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评估
    if p2 > 3:
        return f'{p1}%,连续{abs(int(p2))}周上升'
    elif p2 < -3:
        return f'{p1}%,连续{abs(int(p2))}周下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendFund_RAISE_RATIO_181500000001_418100000002():
    """
    指数.融资余额/流通市值比例函数

    Returns:
    - str: 如果 p2>0.8 则返回"处{p1}%历史高位"，如果 p2<0.2 则返回"处{p1}%历史高位"，否则返回空字符串
    """
    # 逐一取得指标值
    p1 = get_factor_value(181500000001)
    p2 = get_factor_value(418100000002)

    # 检查 p_value 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评估
    if p2 > 0.8:
        return f'处{p1}%历史高位'
    elif p2 < 0.2:
        return f'处{p1}%历史高位'
    else:
        return ''  # 其他情况返回空字符串
def MarketTrendFund_MANAGEMENT_RATIO_240800000021_417700000003():
    """
    指数.近1月管理层增持比例函数

    Returns:
    - str: 如果 p2>3 则返回"{p1}%,连续int(p2)周上升"，如果 p2<-3 则返回"{p1}%,连续int(p2)周下降"，否则返回空字符串
    """
    # 逐一取得指标值
    p1 = get_factor_value(240800000021)
    p2 = get_factor_value(417700000003)

    # 检查 p_value 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评估
    if p2 > 3:
        return f'{p1}%,连续{abs(int(p2))}周上升'
    elif p2 < -3:
        return f'{p1}%,连续{abs(int(p2))}周下降'
    else:
        return ''  # 其他情况返回空字符串


def MarketTrendFund_RAISE_RATIO_418100000003():
    """
    指数.融资余额/流通市值比例边际趋势(周)函数

    Returns:
    - str: 如果 p>3 则返回"连续int(p)周上升"，如果 p<-3 则返回"连续int(p)周下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(418100000003)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}周上升'
    elif p < -3:
        return f'连续{abs(int(p))}周下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendFund_BEIXIANG_417400000001():
    """
    指数.近1月北向资金净流入占流通市值比边际趋势函数

    Returns:
    - str: 如果 p>3 则返回"连续int(p)周上升"，如果 p<-3 则返回"连续int(p)周下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(417400000001)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}周上升'
    elif p < -3:
        return f'连续{abs(int(p))}周下降'
    else:
        return ''  # 其他情况返回空字符串



def MarketTrendFundText():
    FUND_RATIO_TEXT = ""
    FUND_RATIO_TEXT += MarketTrendFund_FUND_RATIO_416800000002()
    FUND_RATIO_TEXT += MarketTrendFund_FUND_RATIO_416800000001()

    RAISE_RATIO_TEXT = ""
    RAISE_RATIO_TEXT += MarketTrendFund_RAISE_RATIO_418100000003()
    RAISE_RATIO_TEXT += MarketTrendFund_RAISE_RATIO_181500000001_418100000002()

    MANAGEMENT_TEXT = ""
    MANAGEMENT_TEXT += MarketTrendFund_MANAGEMENT_RATIO_240800000021_417700000003()
    
    LGT_TEXT = ""
    LGT_TEXT += MarketTrendFund_LGT_RATIO_417300000002()
    LGT_TEXT += MarketTrendFund_LGT_RATIO_417300000002()

    BUYBACK_TEXT = ""
    BUYBACK_TEXT += MarketTrendFund_BUYBACK_RATIO_240800000022_417800000003()


    BEIXIANG_TEXT = ""
    BEIXIANG_TEXT += MarketTrendFund_BEIXIANG_417400000001()

    result_text = "资金："
    if FUND_RATIO_TEXT:
        result_text += "主动偏股型基金持仓占比" + FUND_RATIO_TEXT + "；"

    if MANAGEMENT_TEXT:
        result_text += "近1月管理层增持比例" + RAISE_RATIO_TEXT + "；"

    if LGT_TEXT:
        result_text += "陆股通持股比例" + LGT_TEXT + "；"

    if BUYBACK_TEXT:
        result_text += "近1月回购比例" + BUYBACK_TEXT + "；"

    if BEIXIANG_TEXT:
        result_text += "近1月北向资金净流入占流通市值比" + BEIXIANG_TEXT + "；"

    if result_text == "资金：":
        result_text = ''
    else:
        result_text = result_text[:-1] + "。"

    return result_text

x4 = MarketTrendFundText()
print(x4)


def MarketTrendTech_CROWD_418600000002():
    """
    指数.交易拥挤度历史分位函数

    Returns:
    - str: 如果 p>0.8 则返回"处{p}%历史高位"，如果 p<0.2 则返回"处{p}%历史高位"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(418600000002)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 0.8:
        return f'处{p}%历史高位'
    elif p < 0.2:
        return f'处{p}%历史高位'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_CROWD_418600000003():
    """
    指数.交易拥挤度边际趋势(周)函数

    Returns:
    - str: 如果 p>3 则返回"连续abs(int(p))周上升"，如果 p<-3 则返回"连续abs(int(p))周下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(418600000003)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}周上升'
    elif p < -3:
        return f'连续{abs(int(p))}周下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_EARNING_RATIO_400300000002():
    """
    指数.近1年收益率历史分位函数

    Returns:
    - str: 如果 p>0.8 则返回"处{p}%历史高位"，如果 p<0.2 则返回"处{p}%历史高位"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(400300000002)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 0.8:
        return f'处{p}%历史高位'
    elif p < 0.2:
        return f'处{p}%历史高位'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_EARNING_RATIO_400300000003():
    """
    指数.近1年收益率边际趋势(周)函数

    Returns:
    - str: 如果 p>3 则返回"连续abs(int(p))周上升"，如果 p<-3 则返回"连续abs(int(p))周下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(400300000003)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}周上升'
    elif p < -3:
        return f'连续{abs(int(p))}周下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_CLOSE50_240800000013_416400000003():
    """
    指数.创50日新低的个股占比函数

    Returns:
    - str: 如果 p2=-1 则返回"今日有{p1}%个股创50日新低,连续abs(int(p2))周上升"，否则返回空字符串
    """
    # 获取指标值
    p1 = get_factor_value(240800000013)
    p2 = get_factor_value(416400000003)

    # 检查 p_value 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评估
    if p2 == -1:
        return f'今日有{p1}%个股创50日新低,连续{abs(int(p2))}周上升'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_CLOSE120_416200000002():
    """
    指数.120日均线上方个股占比历史分位函数

    Returns:
    - str: 如果 p>0.8 则返回"处{p}%历史高位"，如果 p<0.2 则返回"处{p}%历史高位"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(416200000002)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 0.8:
        return f'处{p}%历史高位'
    elif p < 0.2:
        return f'处{p}%历史高位'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_CLOSE120_416200000003():
    """
    指数.120日均线上方个股占比边际趋势(周)函数

    Returns:
    - str: 如果 p>3 则返回"连续abs(int(p))周上升"，如果 p<-3 则返回"连续abs(int(p))周下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(416200000003)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}周上升'
    elif p < -3:
        return f'连续{abs(int(p))}周下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_VOLUME_RATIO_99000000001_400500000003():
    """
    指数.量比变化(50交易日)函数

    Returns:
    - str: 根据逻辑返回不同的描述，如果 p2=50 则返回"量比变化{p1}%，创50日新高"，如果 p2=-50 则返回"量比变化{p1}%，创50日新低"，
           如果 p2=200 则返回"量比变化{p1}%，创200日新高"，如果 p2=-200 则返回"量比变化{p1}%，创200日新低"，否则返回空字符串
    """
    # 获取指标值
    p1 = get_factor_value(99000000001)
    p2 = get_factor_value(400500000003)

    # 检查 p_value 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评估
    if p2 == 50:
        return f'量比变化{p1}%，创50日新高'
    elif p2 == -50:
        return f'量比变化{p1}%，创50日新低'
    elif p2 == 200:
        return f'量比变化{p1}%，创200日新高'
    elif p2 == -200:
        return f'量比变化{p1}%，创200日新低'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_VOLUME_RATIO_400500000004():
    """
    指数.量比变化(50交易日)边际趋势(周)函数

    Returns:
    - str: 根据逻辑返回不同的描述，如果 p>3 则返回"连续abs(int(p))周上升"，如果 p<-3 则返回"连续abs(int(p))周下降"，否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(400500000004)

    # 检查 p_value 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))}周上升'
    elif p < -3:
        return f'连续{abs(int(p))}周下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_CLOSE180():
    """
    指数.近180日买入评级的个股占比函数

    Returns:
    - str: 根据逻辑返回不同的描述，如果 p2=50 则返回"近180日买入评级的个股占比{p1}%，创50日新高"，
           如果 p2=-50 则返回"近180日买入评级的个股占比{p1}%，创50日新低"，
           如果 p2=200 则返回"近180日买入评级的个股占比{p1}%，创200日新高"，
           如果 p2=-200 则返回"近180日买入评级的个股占比{p1}%，创200日新低"，
           否则返回空字符串
    """
    # 获取指标值
    p1 = get_factor_value(240800000028)
    p2 = get_factor_value(418200000003)

    # 检查 p1 和 p2 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评估
    if p2 == 50:
        return f'近180日买入评级的个股占比{p1}%，创50日新高'
    elif p2 == -50:
        return f'近180日买入评级的个股占比{p1}%，创50日新低'
    elif p2 == 200:
        return f'近180日买入评级的个股占比{p1}%，创200日新高'
    elif p2 == -200:
        return f'近180日买入评级的个股占比{p1}%，创200日新低'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_CLOSE181():
    """
    指数.近180日买入评级的个股占比_边际趋势(周)函数

    Returns:
    - str: 根据逻辑返回不同的描述，如果 p>3 则返回"连续{abs(int(p))} 周上升"，
           如果 p<-3 则返回"连续{abs(int(p))} 周下降"，
           否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(418200000004)

    # 检查 p 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))} 周上升'
    elif p < -3:
        return f'连续{abs(int(p))} 周下降'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_PREMIUM_RISK():
    """
    指数.股权风险溢价函数

    Returns:
    - str: 根据逻辑返回不同的描述，如果 p2=50 则返回"股权风险溢价{p1}%：创50日新高"，
           如果 p2=-50 则返回"股权风险溢价{p1}%：创50日新低"，
           如果 p2=200 则返回"股权风险溢价{p1}%：创200日新高"，
           如果 p2=-200 则返回"股权风险溢价{p1}%：创200日新低"，
           否则返回空字符串
    """
    # 获取指标值
    p1 = get_factor_value(178000000000)
    p2 = get_factor_value(178200000001)

    # 检查 p1 和 p2 是否为 None
    if p1 is None or p2 is None:
        return ''

    # 根据逻辑进行评估
    if p2 == 50:
        return f'股权风险溢价{p1}%：创50日新高'
    elif p2 == -50:
        return f'股权风险溢价{p1}%：创50日新低'
    elif p2 == 200:
        return f'股权风险溢价{p1}%：创200日新高'
    elif p2 == -200:
        return f'股权风险溢价{p1}%：创200日新低'
    else:
        return ''  # 其他情况返回空字符串

def MarketTrendTech_PREMIUM_RISK_weekly_trend():
    """
    指数.股权风险溢价边际趋势(周)函数

    Returns:
    - str: 根据逻辑返回不同的描述，如果 p>3 则返回"连续{abs(int(p))} 周上升"，
           如果 p<-3 则返回"连续{abs(int(p))} 周下降"，
           否则返回空字符串
    """
    # 获取指标值
    p = get_factor_value(178200000002)

    # 检查 p 是否为 None
    if p is None:
        return ''

    # 根据逻辑进行评估
    if p > 3:
        return f'连续{abs(int(p))} 周上升'
    elif p < -3:
        return f'连续{abs(int(p))} 周下降'
    else:
        return ''  # 其他情况返回空字符串


def MarketTrendTechText():
    TECH_CROWD_TEXT = ""
    TECH_CROWD_TEXT += MarketTrendTech_CROWD_418600000002()
    TECH_CROWD_TEXT += MarketTrendTech_CROWD_418600000003()

    TECH_EARNING_TEXT = ""
    TECH_EARNING_TEXT += MarketTrendTech_EARNING_RATIO_400300000002()
    TECH_EARNING_TEXT += MarketTrendTech_EARNING_RATIO_400300000003()

    TECH_CLOSE50 = ""
    TECH_CLOSE50 += MarketTrendTech_CLOSE50_240800000013_416400000003()

    TEXT_CLOSE180 = ""
    TEXT_CLOSE180 += MarketTrendTech_CLOSE180()


    TEXT_CLOSE181 = ""
    TEXT_CLOSE181 += MarketTrendTech_CLOSE181()

    TECH_CLOSE120 = ""
    TECH_CLOSE120 += MarketTrendTech_CLOSE120_416200000002()
    TECH_CLOSE120 += MarketTrendTech_CLOSE120_416200000003()

    result_text = "情绪/技术："
    if TECH_CROWD_TEXT:
        result_text += "交易拥挤度：" + TECH_CROWD_TEXT + "；"

    if TECH_EARNING_TEXT:
        result_text += "近一年收益率" + TECH_EARNING_TEXT + "；"

    if TECH_CLOSE50:
        result_text += TECH_CLOSE50 + "；"

    if TEXT_CLOSE180:
        result_text +=  TEXT_CLOSE180 + "；"

    if TEXT_CLOSE181:
        result_text +=  TEXT_CLOSE181 + "；"

    if result_text == "情绪/技术：":
        result_text = ''
    else:
        result_text = result_text[:-1] + "。"

    return result_text


x5 = MarketTrendTechText()
print(x5)


def generate_market_status_text():
    """
    生成市场状态文本函数

    Returns:
    - str: 返回生成的市场状态文本
    """
    # 获取指标值
    p1 = get_factor_value(240900000000)
    p2 = get_factor_value(178300000017)
    p3 = get_factor_value(185700000010)

    # 定义返回文本的变量
    p1_text = ''
    p2_text = ''
    p3_text = ''

    # 根据逻辑生成文本
    if p1 == 4:
        p1_text = '重拾升势状态，此时市场状态较好'
    elif p1 == 3:
        p1_text = '升势承压状态，此时警惕疲弱征兆'
    elif p1 == 2:
        p1_text = '震荡调整阶段，此时静待市场反弹'
    elif p1 == 1:
        p1_text = '止跌回升状态，此时应关注反转信号'

    if p2 > 0:
        p2_text = f'上涨{p2*100}%'
    elif p2 == 0:
        p2_text = f'持平{p2*100}%'
    elif p2 < 0:
        p2_text = f'下跌{p2*100}%'

    # if p3 > 0:
    #     p3_text = '高于'
    # elif p3 == 0:
    #     p3_text = '持平'
    # elif p3 < 0:
    #     p3_text = '低于'

    # 返回生成的市场状态文本
    # return f'VSignals市场状态显示全A处{p1_text}。中证A股指数近1周{p2_text}，成交量{p3_text}50日平均水平{p3}%。'
    return f'VSignals市场状态显示全A处{p1_text}。中证A股指数近1周{p2_text}'

p3 = get_factor_value(185700000010)
x6 = generate_market_status_text()
print(x6)
# print(p3)


def MarketTrendFinance_EPS_YOY_149800000014():
    """
    指数.EPS(单季度)同比函数

    Returns:
    - str: 返回生成的结果字符串
    """
    # 获取指标值
    p2 = get_factor_value(149800000014)

    # 判断逻辑
    if p2 == 1:
        return '创历史新高'
    elif p2 == -1:
        return '创历史新低'
    else:
        return ''
