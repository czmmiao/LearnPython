def generate_target_text(data):
    result_text = "从综合评分来看，全A指数价格强度评分、资金持仓评分较弱，宏观驱动、收入回报评分已达中性，EPS评分较强，总体评分当前较弱门。中证A股指数呈现以下值得关注的变化："

    for dimension, info in data.items():
        if dimension == '文字':
            continue
        result_text += f"\n{dimension}："

        for aspect, details in info.items():
            if aspect == '文案':
                continue
            result_text += f" {aspect}："

            if '数值' in details:
                result_text += f"{details['数值']}；"
            elif '评分' in details:
                result_text += f"{details['评分']}；"

            if '历史/市场分位' in details:
                result_text += f"低于20%历史分位或高于80%历史/市场分位文案:指标名称处{details['历史/市场分位']}%历史/市场低位/高位；"

            if '评分变化' in details:
                result_text += f"单期上升/下降幅度超过5%以上文案:{details['评分变化']['指标']}评分1: {details['评分变化']['上升/下降']}xx分；"

            if '新高新低' in details:
                result_text += f"指标值创50/200/历史新高/新低文案:{{指标名称为{details['新高新低']['指标']}%，创50/200/历史新高/新低；"

            if '边际变化' in details:
                result_text += f"连续{details['边际变化']['连续周期']} {details['边际变化']['上升/下降']}；"

        result_text = result_text.rstrip('；') + "。"

    return result_text


# 示例用法
target_data = {
    '文字': '从综合评分来看，全A指数价格强度评分、资金持仓评分较弱，宏观驱动、收入回报评分已达中性，EPS评分较强，总体评分当前较弱门。中证A股指数呈现以下值得关注的变化[2.',
    '全A指数': {
        'EPS成长评分': {'评分': '较弱'},
        '收入回报评分': {'评分': '中性'},
        '技术分析评分': {'评分': '较强'},
        '资金持仓评分': {'评分': '较弱'},
        '估值分析评分': {'评分': '较强'},
        '宏观产业评分': {'评分': '中性'},
        '文案': '展示分别展示全A指数: EPS成长评分、收入回报评分、技术分析评分、资金持仓评分、估值分析评分、宏观产业评分等维度中，较弱 (负面) 、中性和较强(正面) 的指标',
    },
    '值得关注的变化': {
        '财务': {
            '1Q23EPS(单季度)': {'同比增速': '创历史新高', '连续上行': '连续3个单季度'},
            '1Q23EPS(TTM)': {'同比增速': '创历史新高高于3年CAGR'},
            '文案': '触发重大变化的指标',
        },
        '业绩预期': {
            'PEG(TTM)': {'倍数': 'xx倍', '市场分位': 'xx%高位', '连续上升': '连续xx周'},
            '文案': '触发重大变化的指标',
        },
        '估值': {
            'PE(TTM)': {'倍数': 'xx倍', '历史低位': 'xx%历史低位', '连续下降': '连续xx周'},
            '文案': '触发重大变化的指标',
        },
        '资金': {
            '主动偏股型基金持仓占比': {'占比': 'xx%历史低位', '连续下降': '连续xx季'},
            '文案': '触发重大变化的指标',
        },
        '情绪/技术': {
            '交易拥挤度': {'百分比': 'xx%历史低位', '连续下降': '连续2周'},
            '近1年收益率': {'百分比': 'xx%历史低位', '连续下降': '连续xxz周'},
            '文案': '触发重大变化的指标',
        },
    },
}

target_text = generate_target_text(target_data)
print(target_text)
