# -*- coding: utf-8 -*-
"""柿饼资讯网（柿饼.cn / xn--9vvp51i.cn）静态站点生成脚本。
运行：python scripts/build_site.py
输出：根目录下的全部页面、news/ 文章、sitemap.xml、robots.txt、404.html。
"""
import os
import html as H

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://xn--9vvp51i.cn"
SITE_NAME = "柿饼资讯网"
SITE_CN = "柿饼.cn"
TAGLINE = "柿饼 · 产地 · 行情 · 养生 · 吃法"
CONTACT_EMAIL = "548827878@qq.com"
SALE_DOMAINS = ["柿饼.cn", "柿饼.中国", "富平柿饼.cn"]


def puny(d):
    return d.encode("idna").decode("ascii")

CATS = {
    "xingye":   {"name": "行业资讯", "desc": "柿饼产业动态、市场格局与行业观察，看懂这门“甜蜜生意”。"},
    "chandi":   {"name": "产地动态", "desc": "走访富平、恭城等柿饼主产区，了解各地品种与工艺特色。"},
    "shichang": {"name": "市场行情", "desc": "价格、渠道与消费趋势分析，帮买卖双方看行情、做判断。"},
    "jiankang": {"name": "健康养生", "desc": "柿饼营养与食用宜忌，吃得明白、吃得安心。"},
    "meishi":   {"name": "美食食谱", "desc": "柿饼的花样吃法与挑选保存技巧，把柿饼吃出更多可能。"},
    "zhishi":   {"name": "柿饼知识", "desc": "柿饼是怎么来的、柿霜是什么，那些常被问到的冷知识。"},
}

NAV = [
    ("index.html", "首页"),
    ("category-xingye.html", "行业资讯"),
    ("category-chandi.html", "产地动态"),
    ("category-shichang.html", "市场行情"),
    ("category-jiankang.html", "健康养生"),
    ("category-meishi.html", "美食食谱"),
    ("category-zhishi.html", "柿饼知识"),
    ("about.html", "关于本站"),
]

ARTICLES = [
    {
        "slug": "shibing-chanye-qushi", "cat": "xingye", "date": "2026-10-21",
        "title": "柿饼产业为何越来越受关注：行业趋势观察",
        "cover": "images/hero-drying.jpg",
        "summary": "从地方土特产到全国性年货与健康零食，柿饼产业正经历消费升级、渠道电商化与品牌化三重变化，本文梳理背后的趋势与挑战。",
        "body": [
            ("p", "过去提到柿饼，很多人想到的是过年走亲戚时的那一袋“甜蜜的土特产”。如今在电商平台和直播间里，柿饼正以流心、溏心、独立小包装等新形态出现在消费者面前，成为秋冬季节的热门零食。"),
            ("h2", "三重变化正在发生"),
            ("p", "消费端：年轻消费者更看重品质与体验，流心柿饼、礼盒装、产地直发成为关键词；柿饼“天然果干、无添加”的属性，也契合了零食健康化的大方向。"),
            ("p", "渠道端：从农贸批发到淘宝、拼多多、抖音直播，产地农户可以直接触达消费者，中间环节缩短，好产区的好货更容易卖出溢价。"),
            ("p", "品牌端：地理标志保护产品、区域公用品牌陆续落地，富平、恭城等产区开始用统一品牌背书，逐渐摆脱“散装论斤卖”的低价形象。"),
            ("h2", "机会与挑战并存"),
            ("ul", [
                "标准化不足：柿饼的大小、柿霜厚度、含水量缺乏统一分级，品质参差不齐；",
                "依赖天气：传统晾晒工艺受秋冬季天气影响大，阴雨年份损耗明显；",
                "保鲜难题：柿饼怕高温、怕受潮，长途运输和仓储损耗高；",
                "同质化竞争：部分产区低价内卷，挤压优质产品的利润空间。",
            ]),
            ("h2", "结语"),
            ("p", "柿饼产业正从“土特产”走向“品牌化农产品”，对产区、商家和内容创作者来说，品质与信任仍是长期竞争的核心。柿饼资讯网将持续关注行业动态，为大家带来及时、实用的柿饼资讯。"),
        ],
    },
    {
        "slug": "shibing-chanqu-fenbu", "cat": "xingye", "date": "2026-10-18",
        "title": "一文看懂中国柿饼主要产区与各自特色",
        "cover": "images/fuping-hang.jpg",
        "summary": "富平的流心、恭城的月柿、渑池的牛心柿……中国柿饼主产区各有什么特点？本文按产区为你盘点。",
        "body": [
            ("p", "中国是世界柿子主产国之一，柿子加工成柿饼的历史十分悠久。不同产区的气候、品种与工艺，造就了风味各异的柿饼。"),
            ("h2", "陕西富平：流心柿饼的代表"),
            ("p", "富平地处关中平原与陕北高原的过渡地带，主栽“富平尖柿”，采用吊晒工艺制作。富平柿饼肉质软糯、切开呈流心状，是目前电商上最受关注的柿饼产区之一，产品已获国家地理标志保护。"),
            ("h2", "广西恭城、平乐：月柿与出口"),
            ("p", "广西恭城瑶族自治县主产“月柿”，果实大、肉厚、甜度高，制成的柿饼韧糯耐嚼。除内销外，恭城及周边平乐等地也是传统出口东南亚的重要柿饼货源。"),
            ("h2", "河南渑池：牛心柿之乡"),
            ("p", "河南渑池以牛心柿闻名，当地柿饼多为吊晒与摊晒结合，风味甘甜，还保留着颇具规模的“晒柿饼”传统村落景观。"),
            ("h2", "山东、山西、福建、云南等地"),
            ("p", "山东曹县等地以柿霜厚实的霜饼著称；山西孝义一带也有悠久的柿饼传统；福建永定、云南保山等地则结合当地柿种加工，风味各有不同。"),
            ("note", "产区与工艺差异直接影响柿饼的口感、糖度和柿霜厚度，选购时可结合产地信息作参考。"),
        ],
    },
    {
        "slug": "fuping-shibing", "cat": "chandi", "date": "2026-10-15",
        "title": "陕西富平柿饼：从宫廷贡品到地理标志产品",
        "cover": "images/fuping-hang.jpg",
        "summary": "富平柿饼凭什么出名？从流传的宫廷贡品故事到国家地理标志保护产品，尖柿品种、吊晒工艺与流心口感，一起来看。",
        "body": [
            ("p", "提到中国柿饼，“富平”往往是第一个被想起的名字。富平位于陕西渭北旱塬，种植柿子已有上千年历史，当地流传着柿饼曾作为贡品进献宫廷的说法。"),
            ("h2", "尖柿与吊晒工艺"),
            ("p", "富平主栽“富平尖柿”，果形尖顶、个大肉厚、含糖量高。当地采用吊晒工艺：去皮后的柿子用绳子串起悬挂晾晒，配合多次“捏心”整形，历时约四十天，成品软糯流心、甜而不腻。"),
            ("h2", "地理标志与品牌化"),
            ("p", "富平柿饼已成为国家地理标志保护产品，富平也被誉为“中国柿乡”。近年来，富平柿饼在电商渠道走红，“流心”成为其最深入人心的标签。"),
            ("h2", "选购提示"),
            ("p", "正宗富平流心柿饼一般个头较大、表皮橙红、切开后内部溏心明显。购买时注意辨别产地，观察柿霜是否均匀，并选择有资质的商家。"),
        ],
    },
    {
        "slug": "gongcheng-yueshi", "cat": "chandi", "date": "2026-10-12",
        "title": "广西恭城月柿：另一张中国柿饼名片",
        "cover": "images/gongcheng-slice.jpg",
        "summary": "与富平流心柿不同，广西恭城月柿以“个大、肉厚、韧糯”著称，还是传统出口东南亚的柿饼货源。",
        "body": [
            ("p", "在陕西富平之外，广西恭城是另一张响亮的柿饼名片。恭城瑶族自治县种柿历史悠久，“月柿”因成熟后果形饱满、色泽似月而得名，是国家地理标志保护产品。"),
            ("h2", "月柿与柿饼工艺"),
            ("p", "月柿果实大、皮薄肉厚。加工柿饼时多采用去皮后晾晒或烘烤的方式，成品色泽金黄至琥珀色，肉质韧糯、甜度高，耐咀嚼、耐储存。"),
            ("h2", "出口与产业基础"),
            ("p", "恭城及周边平乐等地是传统柿饼出口基地，产品远销东南亚市场。近年来，产地也通过电商直播“产地直发”，把恭城柿饼卖向全国。"),
            ("p", "相比富平的软糯流心，恭城月柿柿饼更偏“嚼劲”路线，两种风格满足了不同消费者的偏好。"),
        ],
    },
    {
        "slug": "shibing-jiage-yinsu", "cat": "shichang", "date": "2026-10-09",
        "title": "柿饼价格为什么差这么多：影响价格的主要因素",
        "cover": "images/market-box.jpg",
        "summary": "从十几块到几十上百元一斤，柿饼价差背后的品种、产地、品级与渠道逻辑，一次讲清。",
        "body": [
            ("p", "市面上的柿饼，价格从每斤十几元到几十元甚至上百元都有。价差背后，其实是品种、产地、品级、渠道等一系列因素叠加的结果。"),
            ("h2", "品种与产区"),
            ("p", "不同柿子品种的含糖量、肉质与出霜率不同，加工成本也不一样；富平尖柿、广西月柿等名优品种，价格通常高于普通品种。"),
            ("h2", "年份与天气"),
            ("p", "传统晾晒高度依赖秋冬季天气：光照好、干燥的年份出霜好、损耗低；遇到阴雨则易霉变减产，价格随之走高。"),
            ("h2", "品级与工艺"),
            ("p", "个头大小、柿霜厚薄、果形是否完整、有无裂口，都会影响等级；手工吊晒、多次捏心的工艺耗时更长，成本也更高。"),
            ("h2", "渠道与品牌"),
            ("p", "产地直采通常比层层批发便宜，而带品牌、礼盒包装、冷链发货的产品，会包含更高的附加成本。"),
            ("note", "柿饼价格随产区、年份、品级浮动，不同平台报价差异大。购买时建议按“产地＋品级＋工艺”综合比价，警惕过低价格。"),
        ],
    },
    {
        "slug": "shibing-dianshang-qudao", "cat": "shichang", "date": "2026-10-06",
        "title": "电商时代，柿饼销售渠道正在怎么变",
        "cover": "images/market-box.jpg",
        "summary": "直播带货、产地直发、礼盒定制……柿饼正从农贸市场走向直播间，渠道变迁对买卖双方意味着什么？",
        "body": [
            ("p", "过去买柿饼，要么赶集，要么去农贸市场。如今，柿饼的主要销售阵地正在转向线上。"),
            ("h2", "直播与短视频带货"),
            ("p", "秋冬是柿饼销售旺季，不少产地农户和商家通过抖音、淘宝等平台直播“开箱流心柿饼”，直观的视觉冲击让柿饼迅速出圈，产地直发成为主流卖点。"),
            ("h2", "平台与礼盒化"),
            ("p", "电商平台上的柿饼从散装走向小包装、独立装和礼盒装，送礼场景增多；中秋、春节等节点是柿饼礼盒的销售高峰。"),
            ("h2", "供应链升级"),
            ("p", "快递冷链与防震包装让“流心”柿饼也能长途运输；与此同时，平台对食品资质、检测报告的要求，也在倒逼商家规范经营。"),
            ("p", "对消费者来说，渠道变多意味着选择更多、比价更容易；对商家来说，好产品、好内容加上可信的售后，才是长期生意。"),
        ],
    },
    {
        "slug": "shibing-yingyang", "cat": "jiankang", "date": "2026-10-03",
        "title": "柿饼的营养价值与适宜人群",
        "cover": "images/health-tea.jpg",
        "summary": "柿饼富含碳水、膳食纤维与多种维生素，是传统健康零食，但含糖量高，怎么吃更合适？",
        "body": [
            ("p", "柿饼由鲜柿干制而成，营养较为浓缩。它保留了鲜柿中的大部分营养成分，同时因水分减少，糖分和风味更加集中。"),
            ("h2", "主要营养成分"),
            ("ul", [
                "碳水化合物：柿饼含糖量较高，主要为葡萄糖、果糖，可快速补充能量；",
                "膳食纤维：有助于促进肠道蠕动、增加饱腹感；",
                "维生素与矿物质：含有胡萝卜素、维生素C及钾等矿物质；",
                "多酚类物质：柿子中天然含有的多酚类成分，常被提及具有抗氧化价值，具体含量因品种而异。",
            ]),
            ("h2", "适宜人群"),
            ("p", "一般人群均可适量食用。作为传统零食，柿饼适合秋冬时节和节日茶点；运动后或低血糖时少量食用，也能快速补充能量。"),
            ("note", "柿饼本质是高糖食物，热量不低。控制体重、血糖偏高的人群应注意限量；儿童食用需控制数量，并注意食用后的口腔清洁。"),
        ],
    },
    {
        "slug": "shibing-shiji-jinji", "cat": "jiankang", "date": "2026-09-29",
        "title": "柿饼食用禁忌：哪些人不宜多吃、怎么吃更安心",
        "cover": "images/stack-frost.jpg",
        "summary": "柿饼虽甜，但鞣酸、高糖和黏性都需注意。空腹、过量、与高蛋白同食等常见误区一次说清。",
        "body": [
            ("p", "柿饼好吃，但并不是可以“敞开了吃”的零食。以下几条食用注意事项，值得了解。"),
            ("h2", "鞣酸与“胃柿石”"),
            ("p", "柿子（含柿饼）中含有较多鞣酸（单宁）。空腹状态下大量食用，鞣酸可能与胃酸及食物中的蛋白质结合，形成不易消化的团块，民间俗称“胃柿石”。建议饭后少量食用，避免空腹和一次性大量进食。"),
            ("h2", "与高蛋白食物同食需注意"),
            ("p", "传统饮食建议柿子不与螃蟹等高蛋白食物同食，其原理同样是鞣酸遇蛋白质易形成沉淀。虽然并非人人都会出现不适，但肠胃敏感者应留意。"),
            ("h2", "高糖与特殊人群"),
            ("ul", [
                "糖尿病患者：柿饼含糖量高，应在医生或营养师指导下严格控制食用量；",
                "肥胖与控糖人群：需计入每日总热量；",
                "婴幼儿：消化能力弱，不宜多食，且柿饼黏性大，需防止噎呛；",
                "口腔敏感人群：柿饼黏甜，食用后及时漱口。",
            ]),
            ("note", "以上为一般性饮食常识，不构成医疗建议；有基础疾病或肠胃不适者，请遵医嘱。"),
        ],
    },
    {
        "slug": "shibing-chifa", "cat": "meishi", "date": "2026-09-25",
        "title": "柿饼的六种家常吃法，甜而不腻",
        "cover": "images/recipe-board.jpg",
        "summary": "除了直接吃，柿饼还能蒸、烤、炖、入粥、夹坚果。六种家常吃法，让柿饼吃出更多花样。",
        "body": [
            ("h2", "一、直接吃，配茶最搭"),
            ("p", "柿饼本身甜糯，泡一杯清茶边吃边喝，最能体会原味；流心柿饼建议小口咬，感受溏心化开的层次。"),
            ("h2", "二、蒸热吃"),
            ("p", "柿饼隔水蒸三五分钟，果肉变得温热软糯，冬天吃特别舒服；也可以与年糕、八宝饭同蒸。"),
            ("h2", "三、烤着吃"),
            ("p", "烤箱或空气炸锅低温烤几分钟，表面微微焦糖化，风味更浓郁。注意控制温度和时间，别烤过头。"),
            ("h2", "四、柿饼炖银耳汤"),
            ("p", "银耳泡发煮出胶质后，加入剪开的柿饼再炖十几分钟，汤色微甜，是秋冬润燥的经典搭配。"),
            ("h2", "五、柿饼入粥"),
            ("p", "煮小米粥或燕麦粥时放几粒柿饼丁，粥的甜味来自天然果糖，省糖又增香。"),
            ("h2", "六、柿饼夹坚果"),
            ("p", "柿饼对半切开，夹入核桃仁、巴旦木等坚果，软糯裹着香脆，是快手又讨喜的茶点；也可以切片蘸酸奶吃。"),
            ("note", "柿饼含糖量高，入菜入粥后可相应减少糖的用量；以上吃法适合一般人群，控糖人群请酌量。"),
        ],
    },
    {
        "slug": "shibing-tiaoxuan-baocun", "cat": "meishi", "date": "2026-09-21",
        "title": "柿饼怎么挑、怎么存？看霜、看色、看手感",
        "cover": "images/knowledge-single.jpg",
        "summary": "柿霜是不是越多越好？怎么判断柿饼新不新鲜？保存防霉的关键点都在这里。",
        "body": [
            ("h2", "挑选四看"),
            ("ul", [
                "看柿霜：柿霜自然、均匀、细腻者为佳；霜层过厚且一碰就掉粉，可能是人工“滚霜”，要留意；",
                "看色泽：优质柿饼表皮呈自然的橙红或红褐色，颜色过于鲜亮或发暗发黑都要警惕；",
                "看外形：果形完整、无裂口、无霉斑，果蒂干净；",
                "闻味道：应有柿果的甜香，无异味、无酸馊气。",
            ]),
            ("h2", "手感与产季"),
            ("p", "优质柿饼捏起来软硬适中、有弹性；过硬可能干瘪，过软可能受潮。每年秋冬（一般10月之后）是当年新柿饼的上市季节，买新不买旧。"),
            ("h2", "保存要点"),
            ("ul", [
                "阴凉干燥处密封存放，避免高温和阳光直晒；",
                "冷藏可延长保质期，取出回温后尽快食用，避免反复温差；",
                "柿霜不要洗掉，它是天然糖分结晶；",
                "一旦发现霉变、异味或异常黏手，请勿食用。",
            ]),
            ("note", "散装柿饼没有统一保质期，建议按商家标注和实际储存条件判断；真空小包装开袋后尽快吃完。"),
        ],
    },
    {
        "slug": "shibing-zhizuo-gongyi", "cat": "zhishi", "date": "2026-09-18",
        "title": "柿饼是怎么做出来的：传统工艺全流程",
        "cover": "images/rack-drying.jpg",
        "summary": "选果、去皮、晾晒、捏心、回软、出霜——一枚柿饼的诞生要经过哪些步骤？带你了解传统柿饼工艺。",
        "body": [
            ("p", "一枚好柿饼，背后是一整套讲究的工艺。虽然各地做法略有差异，但核心流程大体一致。"),
            ("h2", "第一步：选果"),
            ("p", "选用充分成熟但质地仍偏硬的鲜柿，要求果形端正、无病虫害和机械损伤——太软的柿子无法去皮定型。"),
            ("h2", "第二步：去皮"),
            ("p", "用旋刀或手工削去果皮。去皮要均匀、干净，果皮残留会影响晒制和口感。"),
            ("h2", "第三步：晾晒或吊晒"),
            ("p", "富平等地采用吊晒，去皮柿子串起悬挂，靠秋风和阳光慢慢脱水；广西等地也有摊放在竹匾上晾晒的做法。现代化加工则多使用热风烘干房。"),
            ("h2", "第四步：捏心整形"),
            ("p", "晾晒过程中需要多次“捏心”，把果肉捏软、把果形压扁，促进水分均匀蒸发，也让柿饼口感更均匀。"),
            ("h2", "第五步：回软与出霜"),
            ("p", "柿饼晾至半干后收储回软，再在低温高湿环境下让糖分析出结晶，形成柿饼表面那层白霜。整个过程通常需要三十到四十多天。"),
            ("note", "出霜量与品种、天气、工艺直接相关。霜厚不代表更甜，但通常意味着工艺更精细。"),
        ],
    },
    {
        "slug": "shibing-shuang", "cat": "zhishi", "date": "2026-09-15",
        "title": "柿饼上的白霜是什么？能吃吗",
        "cover": "images/knowledge-single.jpg",
        "summary": "柿饼表面的白霜是发霉还是糖？成分是什么、为什么有的厚有的薄？一文说清。",
        "body": [
            ("p", "很多第一次见到柿饼的人都会问：上面那层白霜是什么，是不是发霉了？答案是：不是霉，而是糖。"),
            ("h2", "柿霜的成分"),
            ("p", "柿霜主要是柿饼在低温环境下，果肉中的葡萄糖、果糖等糖分随水分蒸发析出、在表面结晶形成的，还含有少量甘露醇等物质。它是天然形成的，可以放心食用。"),
            ("h2", "柿霜厚薄的差异"),
            ("p", "出霜量与柿子品种、含糖量、晾晒回软工艺和储存环境有关：糖分高、工艺精细、回软充分的柿饼霜更均匀；人工“滚霜”形成的霜则往往浮于表面、容易掉粉。"),
            ("h2", "柿霜的传统说法"),
            ("p", "在传统食养观念中，柿霜被认为有清热润燥的作用，常用来泡水或直接入口；现代食品科学则主要将其视为糖分结晶，具体功效因人而异。"),
            ("h2", "与霉变的区别"),
            ("ul", [
                "柿霜：白色或淡黄，细腻均匀，无异味，可以吃；",
                "霉变：常呈灰黑、绿褐色斑点，伴有酸馊或霉味，须丢弃。",
            ]),
            ("note", "保存不当受潮的柿饼即使表面无霉斑，也可能内部变质，食用前注意检查。"),
        ],
    },
    {
        "slug": "shibing-yitian-jige", "cat": "jiankang", "date": "2026-10-22",
        "title": "柿饼一天吃几个合适？吃多了会怎样",
        "cover": "images/daily-amount.jpg",
        "summary": "柿饼甜糯好吃，一天吃几个合适？本文给出健康人群、老人和儿童的食用量参考，并说明吃多了可能带来的不适。",
        "body": [
            ("p", "柿饼好吃，但它是高糖、高浓缩的果干，一不注意就容易吃多。一天到底吃几个合适？本文按人群给参考。"),
            ("h2", "一般人群：每天1到3枚为宜"),
            ("p", "健康成年人作为零食，建议每天1到3枚（约30到80克）即可，最好放在正餐后或两餐之间，避免空腹大量食用。"),
            ("h2", "老人与儿童：减半并注意"),
            ("ul", [
                "老年人肠胃功能减弱，一次1枚左右为宜，有糖尿病或胃病者更要谨慎；",
                "3岁以上儿童一次半枚到1枚，柿饼黏性大，要细嚼慢咽，避免噎呛；",
                "糖尿病患者应在医生指导下食用，即使血糖稳定也建议浅尝。",
            ]),
            ("h2", "吃多了可能怎样"),
            ("ul", [
                "糖分摄入过多，容易热量超标、腹胀反酸；",
                "鞣酸摄入过多，空腹时存在形成胃柿石的风险；",
                "柿饼黏性大、含糖高，对牙齿不友好，吃完记得漱口。",
            ]),
            ("note", "柿饼不是“补品”，适量享受风味即可；如果食用后出现腹胀、腹痛持续不缓解，请及时就医。"),
        ],
    },
    {
        "slug": "xianshi-shibing-qubie", "cat": "jiankang", "date": "2026-10-20",
        "title": "鲜柿子和柿饼营养有什么区别？怎么选",
        "cover": "images/fresh-vs-dried.jpg",
        "summary": "鲜柿子含水量高、维生素C保留更多，柿饼糖分浓缩、更耐储存也更甜。两者营养区别和适用场景一次讲清。",
        "body": [
            ("p", "鲜柿子和柿饼是同一种水果的两种形态。加工过程中水分流失，营养被浓缩，但也有一些成分发生了变化。"),
            ("h2", "营养对比"),
            ("ul", [
                "鲜柿：水分足、热量较低、口感脆软，维生素C保留较多；",
                "柿饼：水分大幅减少，碳水化合物和糖分浓缩，单位重量热量更高，膳食纤维、矿物质同样丰富；",
                "鞣酸：柿子成熟和干制过程中鞣酸会下降，但柿饼仍含一定量鞣酸，不宜空腹大量食用。",
            ]),
            ("h2", "风味与场景"),
            ("ul", [
                "鲜柿季节性强、不耐储存，适合当季现吃；",
                "柿饼耐储存、易携带，是秋冬零食和年货；",
                "送礼、长途运输选柿饼；当季尝鲜选鲜柿。",
            ]),
            ("h2", "怎么选"),
            ("p", "看用途：追求清爽低热量选鲜柿；追求浓郁风味、方便储存选柿饼。控糖人群则两者都要控制量，鲜柿相对更“轻盈”。"),
            ("note", "无论鲜柿还是柿饼，都不要空腹大量食用，也不建议与螃蟹等高蛋白食物短时间内同食。"),
        ],
    },
    {
        "slug": "diaobing-yuanbing-qubie", "cat": "zhishi", "date": "2026-10-17",
        "title": "吊柿饼和圆柿饼有什么区别？",
        "cover": "images/hanging-vs-round.jpg",
        "summary": "富平吊柿饼呈长形、软糯流心，广西圆柿饼扁圆、韧糯耐嚼。形态、工艺与口感的区别，一文看懂。",
        "body": [
            ("p", "买柿饼时常看到两种形态：一串串的“吊柿饼”和扁圆的“圆柿饼”。它们的区别不只是外形，还藏着工艺和口感的差异。"),
            ("h2", "吊柿饼：吊挂晾晒，软糯流心"),
            ("p", "吊柿饼以富平尖柿为代表，去皮后整果串起悬挂晾晒，重力让果形自然拉长，脱水后内部呈溏心，吃起来软糯香甜、切开流心，代表产区是陕西富平。"),
            ("h2", "圆柿饼：摊晒整形，扁圆韧糯"),
            ("p", "圆柿饼多为去皮后摊放在竹匾上晾晒，配合捏心压扁成扁圆，以广西月柿、山东柿饼为代表，口感偏韧糯、有嚼劲，适合切片和长期储存。"),
            ("h2", "选购建议"),
            ("ul", [
                "喜欢软糯流心，选吊柿饼，注意认准富平产地与正规商家；",
                "喜欢有嚼劲、耐存放，选圆柿饼；",
                "两种柿饼都要看柿霜是否自然、有无霉变裂口。",
            ]),
        ],
    },
    {
        "slug": "shougong-jigui-qubie", "cat": "zhishi", "date": "2026-10-14",
        "title": "手工柿饼和机器烘干柿饼，哪个更好？",
        "cover": "images/handmade-drying.jpg",
        "summary": "手工晾晒受天气制约但风味传统，机器烘干效率稳定、产量大。两者在工艺、口感、价格上的差别有哪些？",
        "body": [
            ("p", "传统柿饼靠天吃饭，如今越来越多加工环节引入烘干设备。手工和机器做出来的柿饼，到底有什么差别？"),
            ("h2", "手工晾晒：靠天吃饭，风味传统"),
            ("p", "手工柿饼经过去皮、吊晒或摊晒、多次捏心、自然出霜，周期约三十到四十天，受天气影响大、产量有限，但日晒风干的风味自然、柿霜层次丰富。"),
            ("h2", "机器烘干：效率稳定，产量大"),
            ("p", "机器烘干通过热风房控制温度和时间，缩短加工周期、降低阴雨损耗，品质更稳定统一，适合规模化供应；但部分产品为了“好看”会滚霜或高温处理，口感与风味略有差异。"),
            ("h2", "怎么选"),
            ("ul", [
                "追求传统风味和产地体验，选手工柿饼，认准当年新货；",
                "追求稳定品质与性价比，规模化厂家的合格产品也可放心买；",
                "关键看配料表与资质：优质柿饼只有“柿子”，无额外添加。",
            ]),
            ("note", "手工与机器没有绝对高低，看品级、看卫生资质、看是否为当年新货，比纠结工艺更重要。"),
        ],
    },
    {
        "slug": "shibing-pifa-jinhuo", "cat": "shichang", "date": "2026-10-11",
        "title": "柿饼批发怎么选？产地进货渠道与避坑指南",
        "cover": "images/market-stall.jpg",
        "summary": "柿饼进货有哪些渠道？产区直采、批发市场、线上平台分别怎么选？看品级、控损耗、防低价坑，给商家的实用建议。",
        "body": [
            ("p", "每年秋冬是柿饼销售旺季，很多想做柿饼生意的新手都会问：去哪里进货？怎么选不踩坑？本文梳理常见渠道和避坑要点。"),
            ("h2", "常见进货渠道"),
            ("ul", [
                "产区直采：联系富平、恭城、平乐等产区合作社或加工厂，量大价优，适合有稳定销量的商家；",
                "产地批发市场：在产地集散市场现场看货，适合中小批量；",
                "销地批发市场：本地农批市场补货方便，价格略高；",
                "线上批发平台：1688等平台可小批量试单，但务必先拿样、查资质。",
            ]),
            ("h2", "进货看什么"),
            ("ul", [
                "看品级：个头、霜厚、完好度、含水量，按等级谈价；",
                "看损耗：柿饼怕潮怕压，问清包装与冷链，少量试销再大批量；",
                "看资质：食品生产许可、检测报告、包装标签是否齐全；",
                "看价格：明显低于行情的“超低价”要警惕，可能是陈年旧货或劣质货。",
            ]),
            ("h2", "新手建议"),
            ("p", "先少量多渠道拿样对比，锁定一到两家稳定供应商；旺季前备货，注意售后与退换货约定，避免一次性压货。"),
            ("note", "行情随产区、年份、品级波动，本文为一般性经营建议，不构成具体交易承诺。"),
        ],
    },
    {
        "slug": "fuping-shibing-quan-gong-lue", "cat": "chandi", "date": "2026-10-22",
        "title": "富平柿饼为什么出名？流心吊饼的产地、价格与挑选全攻略",
        "cover": "images/fuping-liuxin-guide.jpg",
        "summary": "富平柿饼多少钱一斤、为什么能流心？一文讲清产地、吊饼工艺、等级价格、正宗挑选与保存方法，附常见问题。",
        "body": [
            ("p", "每到秋冬年货季，有一种柿饼总被称作柿饼界的“天花板”——富平柿饼。它产自陕西富平，是国家地理标志产品，以吊挂晾晒、软糯流心、白霜细密闻名。它为什么出名、为什么贵、多少钱一斤、怎么挑到正宗的？这篇文章把产地、工艺、价格、挑选和保存一次讲清。"),
            ("h2", "富平柿饼是什么？产自哪里"),
            ("p", "富平柿饼是陕西省渭南市富平县的特产，以当地传统名优品种富平尖柿为原料加工而成。富平地处渭北高原，是关中平原与陕北黄土高原的过渡地带，光照充足、昼夜温差大，被业内公认为优质柿子优生区。"),
            ("p", "根据《地理标志产品质量要求 富平柿饼》国家标准，其产地保护范围包括富平县城关街道办、东华街道办、淡村镇、流曲镇、到贤镇、宫里镇、曹村镇等乡镇的部分行政村，其中曹村镇是公认的核心产区。"),
            ("p", "富平柿子栽培历史悠久，当地有升底尖柿、辣角尖柿、珠柿、鸡心黄柿等十多个品种，其中最著名、最适合做柿饼的是升底尖柿，被称为尖柿里的“优等生”。"),
            ("h2", "富平柿饼为什么这么出名"),
            ("p", "它之所以出名，靠的是品种、水土和工艺，以及一串硬核的身份背书："),
            ("ul", [
                "2008年，富平柿饼获批国家地理标志产品保护；",
                "2017年，“富平柿饼”成功注册为地理标志证明商标；",
                "2020年，又入选中欧地理标志保护名录；",
                "早在明清两代，当地柿饼就被列为宫廷贡品，有“个大、霜白、底亮、质润、味香甜”五大特色。",
            ]),
            ("p", "加上近年电商和冷链的发展，它从陕西的地方特产走向全国，秋冬季节的“流心柿饼”更成为年货市场上的热门，这也是它价格普遍高于普通柿饼的原因。"),
            ("h2", "富平柿饼为什么能流心"),
            ("p", "富平柿饼最让人惦记的是那一口“溏心”——掰开之后，果肉像琥珀一样晶莹，内里软糯，几乎能拉出糖丝。这并非加了糖，而是品种和工艺共同作用的结果。"),
            ("p", "富平尖柿果个大、果形高，呈心脏形或纺锤形，果肉纤维多、含糖量高。去皮后挂在架上晾晒，柿饼在重力作用下自然拉长，呈纺锤形；晾晒过程中还要反复揉捏柿果，让内部果肉充分糖化、软化，最后捂霜定型，糖心由此形成。"),
            ("p", "这种做法做成的柿饼又叫“吊柿饼”，一排排柿子从架上垂挂下来，是当地秋天的标志性画面。除了纺锤形的吊饼，还有两个柿饼脐脐相对、压成扁圆的“合儿饼”。"),
            ("h2", "一颗吊柿饼是怎么做出来的"),
            ("p", "正宗的富平吊饼坚持自然风干，主要工序大致包括选果、清洗削皮、吊挂日晒、多次捏心（捏晒整形）、定型、捂霜，整个过程要四十天左右，期间还要看天吃饭——光照、通风、湿度都得合适。"),
            ("ul", [
                "削皮：柿果去皮后才能均匀脱水，国标允许柿蒂周围留不超过1厘米宽的果皮；",
                "吊挂：挂架通风晾晒，区别于直接摊在匾上的圆饼；",
                "捏心：晾晒中反复揉捏，帮助果肉软化、糖心形成；",
                "出霜：柿饼在干湿度变化中表面析出葡萄糖和果糖结晶，形成天然白霜。",
            ]),
            ("p", "成品按表面是否有霜分为霜饼和无霜饼：霜饼表面有颗粒状白色糖霜，果肉呈棕红或红褐色；无霜饼果面呈棕红或红褐色。"),
            ("h2", "富平柿饼和普通柿饼有什么区别"),
            ("ul", [
                "形状不同：富平吊饼是纺锤形，广西、平乐一带的圆饼多为扁平圆饼；",
                "口感不同：富平柿饼软糯流心、甜度高；普通圆饼多为韧糯、有嚼劲；",
                "原料不同：富平吊饼用富平尖柿，其他产区多用月柿等品种；",
                "工艺不同：吊饼吊挂晾晒，圆饼多摊晒整形；",
                "价格不同：受品种、产量和地标品牌影响，正宗富平吊饼价格普遍更高。",
            ]),
            ("links", "延伸阅读：", [
                ("吊柿饼和圆柿饼有什么区别？", "diaobing-yuanbing-qubie.html"),
                ("陕西富平柿饼：从宫廷贡品到地理标志产品", "fuping-shibing.html"),
            ]),
            ("h2", "富平柿饼多少钱一斤？等级怎么看"),
            ("p", "吊饼按果个大小定价，习惯上用“每斤多少个”来标规格，个头越大、每斤个数越少，价格越高。以“中国·陕西富平柿子产业指数”公布的行情为例，2025年3月22日，13-15个/斤规格报价约43.47元/斤，6-8个/斤规格约39.43元/斤（不同规格、品级口径不同，会随行情波动）。"),
            ("p", "从零售端看，电商平台上的富平吊饼主流价格多在每斤20-40元，核心产区大果、精品礼盒和霜降后首批新货价格更高；批发平台上普通品级多在每斤15-25元。每年价格还会受到产量、天气和年货行情影响。"),
            ("note", "以上价格为公开行情参考，富平柿饼价格随产区、年份、品级和渠道浮动，购买时请以实际报价为准。"),
            ("p", "买之前还要会看等级：国标对外观、色泽、留皮宽度、有无霉斑损伤等都有要求，正规产品包装上会标注产地、等级、生产许可和地理标志专用标志，信息越全越靠谱。"),
            ("h2", "富平柿饼什么时候上市、去哪买"),
            ("p", "吊饼是典型的时令货：霜降前后（约10月下旬）开始采摘加工，11月到12月集中上市，入冬后到春节前是销售旺季。想吃到流心效果好的新货，建议等11月中旬之后再下单。"),
            ("ul", [
                "尝鲜、送礼：选正规电商平台的产地旗舰店、合作社店铺，认准地理标志和产地；",
                "大量采购：通过富平当地合作社、加工厂或批发渠道，先拿样再批量进货；",
                "线下购买：大型商超、农贸市场的时令专柜，适合现场看霜、摸手感。",
            ]),
            ("links", "延伸阅读：", [
                ("柿饼批发怎么选？产地进货渠道与避坑指南", "shibing-pifa-jinhuo.html"),
            ]),
            ("h2", "怎么挑正宗富平柿饼：三步法"),
            ("p", "北京市消费者协会等机构给出的“三步法”，挑富平吊饼同样适用，再加上认产地，基本不会踩坑："),
            ("ul", [
                "看霜：天然柿霜均匀细腻、像撒了一层细糖粉，轻抖不易大量脱落，入口即化；人工撒的面粉、滑石粉颗粒粗糙、一摸就掉、沾一手白末；",
                "看果肉：优质柿饼果肉呈琥珀色或深橙红、棕红色，颜色自然均匀，发黑、有霉斑的不要买；",
                "摸手感：好柿饼不硬不软，轻捏后能轻微回弹；硬邦邦的是晾晒过度、口感发柴，软塌塌的则水分超标、容易发霉；",
                "闻气味：新鲜柿饼只有自然甜香，有酸味、酒味或霉味的已经变质；",
                "认产地：认准“陕西富平”产地、地理标志专用标志和正规包装，警惕外地圆饼贴牌冒充富平吊饼。",
            ]),
            ("links", "延伸阅读：", [
                ("柿饼上的白霜是什么？是发霉吗", "shibing-shuang.html"),
                ("柿饼怎么挑、怎么存？看霜、看色、看手感", "shibing-tiaoxuan-baocun.html"),
            ]),
            ("h2", "富平柿饼怎么吃、怎么保存"),
            ("p", "富平吊饼开袋即食，常温或冷藏回温后流心更明显。也可以蒸几分钟、夹核桃仁吃，或者切片煮粥、配茶，都是常见吃法。"),
            ("p", "保存记住“防潮、怕热、防冻伤”：短期食用放阴凉干燥处或冰箱冷藏；长期存放可密封冷冻，吃前提前取出回温，避免反复冻融影响口感。"),
            ("links", "延伸阅读：", [
                ("柿饼一天吃几个合适？吃多了会怎样", "shibing-yitian-jige.html"),
                ("柿饼食用禁忌：哪些人不宜多吃", "shibing-shiji-jinji.html"),
            ]),
            ("h2", "常见问题"),
            ("h3", "白霜是发霉吗？"),
            ("p", "不是。天然柿霜是柿饼在干湿度变化中析出的葡萄糖和果糖结晶，颗粒细腻、入口即化；发霉的斑块多呈绿、黑、灰色，伴有霉味，发现霉斑应丢弃。"),
            ("h3", "流心是坏了吗？"),
            ("p", "不是。流心是富平尖柿充分糖化后形成的溏心，是品质的体现；如果柿饼发酸、有酒味或明显霉味，才是变质，不能再吃。"),
            ("h3", "糖尿病人能吃吗？"),
            ("p", "柿饼含糖量高且糖分更易吸收，血糖控制不佳的人群应慎吃或遵医嘱，普通人群也不宜一次吃太多。"),
            ("h3", "为什么有的“富平柿饼”特别便宜？"),
            ("p", "价格明显低于行情，可能是外地圆饼冒充、品级较低、陈年旧货，也可能是人工撒粉或包装信息不全。认准地理标志、产地和正规渠道，别只图便宜。"),
            ("h2", "结语"),
            ("p", "富平柿饼的贵，贵在独有的尖柿品种、四十天的吊挂手工和不可复制的产地水土。买的时候认准产地、看霜摸手感，避开人工撒粉和贴牌货，就能吃到那一口软糯流心的正宗富平吊饼。"),
            ("links", "资料来源：", [
                ("中国·陕西富平柿子产业指数（fpszzs.cn）", "https://www.fpszzs.cn/"),
                ("国家标准《地理标志产品质量要求 富平柿饼》（国家市场监督管理总局）", "https://www.samr.gov.cn/"),
                ("富平县人民政府《富平柿子记》", "http://www.fuping.gov.cn/"),
                ("人民网：柿饼上的白霜洗还是不洗", "http://health.people.com.cn/"),
                ("北京市消费者协会：柿饼选购食用有门道", "http://www.bjxx315.org.cn/"),
            ]),
        ],
    },
]


# ---------------- 工具函数 ----------------

def esc(s):
    return H.escape(s, quote=True)


def fmt_date(d):
    return d[:4] + "年" + d[5:7] + "月" + d[8:10] + "日"


def cat_of(art):
    return CATS[art["cat"]]


def art_url(slug):
    return "news/" + slug + ".html"


def sorted_arts():
    return sorted(ARTICLES, key=lambda a: a["date"], reverse=True)


def arts_of(cat):
    return sorted([a for a in ARTICLES if a["cat"] == cat], key=lambda a: a["date"], reverse=True)


def render_body(blocks):
    out = []
    for b in blocks:
        kind = b[0]
        if kind == "p":
            out.append("<p>" + esc(b[1]) + "</p>")
        elif kind == "h2":
            out.append("<h2>" + esc(b[1]) + "</h2>")
        elif kind == "h3":
            out.append("<h3>" + esc(b[1]) + "</h3>")
        elif kind == "ul":
            items = "".join("<li>" + esc(x) + "</li>" for x in b[1])
            out.append("<ul>" + items + "</ul>")
        elif kind == "note":
            out.append('<div class="note"><strong>提示：</strong>' + esc(b[1]) + "</div>")
        elif kind == "links":
            lis = "".join(
                '<li><a href="' + esc(href) + '">' + esc(text) + "</a></li>"
                for text, href in b[2]
            )
            out.append('<div class="read-more"><strong>' + esc(b[1]) + "</strong><ul>" + lis + "</ul></div>")
    return "\n".join(out)


FAVICON_DATA = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E%3Cpath d='M16 3.2c-.8 0-1.5.6-1.6 1.4-.1.9-.2 1.6-.2 2.5-.2.2-.4.4-.7.6-2.4.4-4.4 1.7-5.6 3.6-1.2 2-1.5 4.5-.8 6.8.8 2.6 2.7 4.8 5.2 6.1 1 .5 2.1.8 3.2.8s2.2-.3 3.2-.8c2.5-1.3 4.4-3.5 5.2-6.1.7-2.3.4-4.8-.8-6.8-1.2-1.9-3.2-3.2-5.6-3.6-.3-.2-.5-.4-.7-.6 0-.9-.1-1.6-.2-2.5-.1-.8-.8-1.4-1.6-1.4z' fill='%23c4501f'/%3E%3Ccircle cx='12' cy='11.5' r='2.6' fill='%23e8884f' opacity='0.8'/%3E%3C/svg%3E"


def head(title, desc, canonical, prefix="", jsonld=""):
    return (
        "<!DOCTYPE html>\n<html lang=\"zh-CN\">\n<head>\n"
        "<meta charset=\"utf-8\">\n"
        '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
        '<meta name="robots" content="index,follow">\n'
        "<title>" + esc(title) + "</title>\n"
        '<meta name="description" content="' + esc(desc) + '">\n'
        '<meta name="keywords" content="柿饼,柿饼资讯,柿饼产地,柿饼价格,柿饼营养价值,柿饼做法">\n'
        '<link rel="canonical" href="' + esc(canonical) + '">\n'
        '<meta property="og:type" content="website">\n'
        '<meta property="og:site_name" content="' + esc(SITE_NAME) + '">\n'
        '<meta property="og:title" content="' + esc(title) + '">\n'
        '<meta property="og:description" content="' + esc(desc) + '">\n'
        '<meta property="og:url" content="' + esc(canonical) + '">\n'
        '<meta property="og:locale" content="zh_CN">\n'
        '<link rel="icon" type="image/svg+xml" href="' + FAVICON_DATA + '">\n'
        '<link rel="stylesheet" href="https://miaoda.feishu.cn/fonts/css2?family=Noto+Serif+SC:wght@600;700;900&family=Noto+Sans+SC:wght@400;500;700&display=swap">\n'
        '<link rel="stylesheet" href="' + prefix + 'css/style.css">\n'
        + jsonld +
        "</head>\n<body>\n"
    )


def jsonld_website():
    return (
        '<script type="application/ld+json">'
        '{"@context":"https://schema.org","@type":"WebSite","name":"' + SITE_NAME + '",'
        '"url":"' + DOMAIN + '/","description":"柿饼资讯网：柿饼行业资讯、产地动态、市场行情、健康养生与美食食谱。"}'
        "</script>"
    )


def jsonld_article(art):
    url = DOMAIN + "/" + art_url(art["slug"])
    data = {
        "@context": "https://schema.org",
        "@type": "NewsArticle",
        "headline": art["title"],
        "description": art["summary"],
        "datePublished": art["date"],
        "image": DOMAIN + "/" + art["cover"],
        "mainEntityOfPage": {"@type": "WebPage", "@id": url},
        "author": {"@type": "Organization", "name": "柿饼资讯网编辑部"},
        "publisher": {"@type": "Organization", "name": SITE_NAME, "logo": {"@type": "ImageObject", "url": DOMAIN + "/favicon.svg"}},
        "articleSection": cat_of(art)["name"],
    }
    bread = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "首页", "item": DOMAIN + "/"},
            {"@type": "ListItem", "position": 2, "name": cat_of(art)["name"], "item": DOMAIN + "/category-" + art["cat"] + ".html"},
            {"@type": "ListItem", "position": 3, "name": art["title"], "item": url},
        ],
    }
    return (
        '<script type="application/ld+json">' + json_dumps(data) + "</script>"
        '<script type="application/ld+json">' + json_dumps(bread) + "</script>"
    )


def json_dumps(obj):
    import json as _j
    return _j.dumps(obj, ensure_ascii=False)


def header_html(prefix, active=None):
    nav = []
    for href, name in NAV:
        cls = ' class="active"' if (active == href or (active and active == name)) else ""
        nav.append('<a href="' + prefix + href + '"' + cls + ">" + name + "</a>")
    date_js = (
        '<script>'
        "(function(){var d=new Date();var s=d.getFullYear()+'年'+(d.getMonth()+1)+'月'+d.getDate()+'日 '+"
        "'星期'+'日一二三四五六'.charAt(d.getDay());var el=document.getElementById('site-date');"
        "if(el){el.textContent=s;}})();"
        "</script>"
    )
    return (
        '<header class="masthead">\n'
        '<div class="container masthead-inner">\n'
        '<a class="brand" href="' + prefix + 'index.html">\n'
        '<svg class="brand-mark" viewBox="0 0 32 32" aria-hidden="true"><path d="M16 3.2c-.8 0-1.5.6-1.6 1.4-.1.9-.2 1.6-.2 2.5-.2.2-.4.4-.7.6-2.4.4-4.4 1.7-5.6 3.6-1.2 2-1.5 4.5-.8 6.8.8 2.6 2.7 4.8 5.2 6.1 1 .5 2.1.8 3.2.8s2.2-.3 3.2-.8c2.5-1.3 4.4-3.5 5.2-6.1.7-2.3.4-4.8-.8-6.8-1.2-1.9-3.2-3.2-5.6-3.6-.3-.2-.5-.4-.7-.6 0-.9-.1-1.6-.2-2.5-.1-.8-.8-1.4-1.6-1.4z" fill="#e8a04f"/><circle cx="12" cy="11.5" r="2.6" fill="#f2b56a" opacity="0.9"/></svg>\n'
        '<span class="brand-name">' + SITE_NAME + '<small class="brand-domain">' + SITE_CN + "</small></span>\n"
        "</a>\n"
        '<div class="masthead-meta"><span id="site-date">今日日期</span><span class="tagline">' + TAGLINE + "</span></div>\n"
        "</div>\n"
        '<nav class="mainnav"><div class="container nav-inner">' + "".join(nav) + "</div></nav>\n"
        + date_js +
        "</header>\n"
    )


def footer_html(prefix):
    hot = sorted_arts()[:4]
    hot_links = "".join(
        '<a href="' + prefix + art_url(a["slug"]) + '">' + esc(a["title"]) + "</a>" for a in hot
    )
    cat_links = "".join(
        '<a href="' + prefix + "category-" + c + '.html">' + CATS[c]["name"] + "</a>" for c in CATS
    )
    return (
        '<footer class="footer">\n'
        '<div class="container footer-grid">\n'
        '<div class="footer-col"><div class="footer-brand">' + SITE_NAME + " <small>" + SITE_CN + "</small></div>"
        "<p>专注柿饼行业资讯、产地动态、市场行情、健康养生与美食食谱的中文资讯站。</p></div>\n"
        '<div class="footer-col"><h4>内容栏目</h4>' + cat_links + "</div>\n"
        '<div class="footer-col"><h4>热门文章</h4>' + hot_links + "</div>\n"
        '<div class="footer-col"><h4>关于本站</h4>'
        '<a href="' + prefix + 'about.html">关于我们</a>'
        '<a href="' + prefix + 'about.html#domains">域名出售出租</a>'
        '<a href="' + prefix + 'about.html#contact">投稿与合作</a>'
        '<a href="' + prefix + 'about.html#statement">免责声明</a>'
        '<a href="mailto:' + CONTACT_EMAIL + '">' + CONTACT_EMAIL + "</a>"
        "</div>\n"
        "</div>\n"
        '<div class="footer-bottom">© 2026 ' + SITE_NAME + "（" + SITE_CN + "） · 本站内容仅供一般参考，不构成医疗或投资建议 · ICP备案号：待办理</div>\n"
        "</footer>\n"
    )


def news_card(a, prefix):
    return (
        '<article class="news-card">\n'
        '<a href="' + prefix + art_url(a["slug"]) + '"><img src="' + prefix + a["cover"] + '" alt="' + esc(a["title"]) + '" loading="lazy"></a>\n'
        '<div class="card-body">\n'
        '<span class="card-tag"><span class="dot">◆</span>' + cat_of(a)["name"] + "</span>\n"
        '<h3 class="card-title"><a href="' + prefix + art_url(a["slug"]) + '">' + esc(a["title"]) + "</a></h3>\n"
        '<p class="card-excerpt">' + esc(a["summary"]) + "</p>\n"
        '<span class="card-meta">' + fmt_date(a["date"]) + "</span>\n"
        "</div>\n</article>\n"
    )


# ---------------- 页面渲染 ----------------

def render_index():
    arts = sorted_arts()
    featured = arts[0]
    hero = (
        '<section class="hero">\n'
        '<div class="container">\n'
        '<a class="hero-card" href="' + art_url(featured["slug"]) + '">\n'
        '<img src="' + featured["cover"] + '" alt="' + esc(featured["title"]) + '">\n'
        '<div class="hero-mask">\n'
        '<span class="tag">' + cat_of(featured)["name"] + "</span>\n"
        "<h1>" + esc(featured["title"]) + "</h1>\n"
        '<p class="hero-excerpt">' + esc(featured["summary"]) + "</p>\n"
        '<span class="hero-date">' + fmt_date(featured["date"]) + ' · <span class="hero-more">阅读全文</span></span>\n'
        "</div>\n</a>\n</div>\n</section>\n"
    )

    tiles = []
    for c, meta in CATS.items():
        tiles.append(
            '<a class="cat-tile" href="category-' + c + '.html"><span class="tile-count">' + str(len(arts_of(c))) + "篇</span>"
            '<span class="tile-name">' + meta["name"] + "</span>"
            '<p class="tile-desc">' + meta["desc"] + "</p></a>\n"
        )

    cards = "".join(news_card(a, "") for a in arts)

    spot_arts = [next(a for a in arts if a["slug"] == "fuping-shibing"), next(a for a in arts if a["slug"] == "gongcheng-yueshi")]
    spots = "".join(
        '<a class="spot-card" href="' + art_url(a["slug"]) + '"><img src="' + a["cover"] + '" alt="' + esc(a["title"]) + '" loading="lazy">'
        '<div class="spot-mask"><span class="tag">' + cat_of(a)["name"] + "</span>"
        "<h3>" + esc(a["title"]) + "</h3><p>" + esc(a["summary"]) + "</p></div></a>\n"
        for a in spot_arts
    )

    body = (
        hero
        + '<section class="section"><div class="container">\n'
        '<div class="section-head"><div><span class="kicker">COLUMNS</span><h2 class="section-title">栏目速览</h2></div></div>\n'
        '<div class="cat-tiles">' + "".join(tiles) + "</div>\n</div></section>\n"
        + '<section class="section"><div class="container">\n'
        '<div class="section-head"><div><span class="kicker">NEWS</span><h2 class="section-title">最新资讯</h2></div>'
        '<a class="section-more" href="category-xingye.html">更多资讯</a></div>\n'
        '<div class="grid-news">' + cards + "</div>\n</div></section>\n"
        + '<section class="section"><div class="container">\n'
        '<div class="section-head"><div><span class="kicker">ORIGIN</span><h2 class="section-title">产地特写</h2></div></div>\n'
        '<div class="spot-grid">' + spots + "</div>\n</div></section>\n"
        + '<section class="section"><div class="container">\n'
        '<div class="about-band">\n'
        "<h2>关于柿饼资讯网</h2>\n"
        "<p>柿饼资讯网（柿饼.cn）专注于柿饼领域的原创资讯：行业趋势、产区故事、行情分析、养生知识与美食做法。我们坚持内容真实、来源可溯，为读者提供有价值的柿饼信息。</p>\n"
        '<a class="btn" href="about.html">了解更多</a>\n'
        "</div>\n</div></section>\n"
    )

    page = (
        head(SITE_NAME + "｜柿饼行业资讯·产地·行情·养生·吃法",
             "柿饼资讯网（柿饼.cn）：专注柿饼行业资讯、产地动态（富平、恭城等）、市场行情、健康养生与美食食谱，每天更新柿饼相关知识。",
             DOMAIN + "/", "", jsonld_website())
        + header_html("")
        + "<main>" + body + "</main>\n"
        + footer_html("")
        + "</body>\n</html>\n"
    )
    return page


def render_category(cat):
    meta = CATS[cat]
    arts = arts_of(cat)
    cards = "".join(news_card(a, "") for a in arts)
    body = (
        '<section class="cat-head"><div class="container">\n'
        '<nav class="breadcrumb"><a href="index.html">首页</a> › <span>' + meta["name"] + "</span></nav>\n"
        "<h1>" + meta["name"] + "</h1>\n<p>" + meta["desc"] + "</p>\n"
        "</div></section>\n"
        '<section class="section"><div class="container"><div class="grid-news">' + cards + "</div></div></section>\n"
    )
    page = (
        head(meta["name"] + "｜" + SITE_NAME, meta["name"] + "：" + meta["desc"], DOMAIN + "/category-" + cat + ".html")
        + header_html("", "category-" + cat + ".html")
        + "<main>" + body + "</main>\n"
        + footer_html("")
        + "</body>\n</html>\n"
    )
    return page


def render_article(a):
    meta = cat_of(a)
    blocks = render_body(a["body"])
    same = [x for x in arts_of(a["cat"]) if x["slug"] != a["slug"]][:2]
    related = ""
    if same:
        related = (
            '<section class="related"><div class="container"><h2>相关阅读</h2>\n'
            '<div class="grid-news">' + "".join(news_card(x, "../") for x in same) + "</div></div></section>\n"
        )
    body = (
        '<section class="page-wrap"><div class="container">\n'
        '<nav class="breadcrumb"><a href="../index.html">首页</a> › '
        '<a href="../category-' + a["cat"] + '.html">' + meta["name"] + "</a> › "
        "<span>" + esc(a["title"]) + "</span></nav>\n"
        '<header class="article-header">\n'
        '<div class="tag-row"><span class="tag-chip">' + meta["name"] + "</span></div>\n"
        "<h1>" + esc(a["title"]) + "</h1>\n"
        '<div class="article-meta"><span>柿饼资讯网编辑部</span><span class="sep">｜</span><span>' + fmt_date(a["date"]) + "</span></div>\n"
        "</header>\n"
        '<figure class="article-cover"><img src="../' + a["cover"] + '" alt="' + esc(a["title"]) + '">'
        "<figcaption>" + esc(a["title"]) + "</figcaption></figure>\n"
        '<div class="article-body">' + blocks + "</div>\n"
        '<div class="article-tags"><span class="tag-chip">' + meta["name"] + "</span><span class=\"tag-chip\">柿饼</span></div>\n"
        "</div></section>\n"
        + related
    )
    page = (
        head(a["title"] + "｜" + SITE_NAME, a["summary"], DOMAIN + "/" + art_url(a["slug"]), "../", jsonld_article(a))
        + header_html("../")
        + "<main>" + body + "</main>\n"
        + footer_html("../")
        + "</body>\n</html>\n"
    )
    return page


def render_about():
    body = (
        '<section class="page-wrap"><div class="container">\n'
        '<nav class="breadcrumb"><a href="index.html">首页</a> › <span>关于本站</span></nav>\n'
        '<header class="article-header"><h1>关于柿饼资讯网</h1>'
        '<div class="article-meta"><span>柿饼.cn · 柿饼资讯网</span></div></header>\n'
        '<div class="article-body">\n'
        "<h2>我们是谁</h2>\n"
        "<p>柿饼资讯网（柿饼.cn）是一家中文柿饼资讯站点，专注柿饼行业的原创内容：行业趋势观察、主产区走访（陕西富平、广西恭城等）、市场价格分析、健康养生知识以及美食食谱。</p>\n"
        "<h2>内容栏目</h2>\n"
        "<ul>\n"
        "<li>行业资讯：柿饼产业动态、市场格局与行业观察；</li>\n"
        "<li>产地动态：主产区品种、工艺与人文故事；</li>\n"
        "<li>市场行情：价格影响因素、渠道变化与消费趋势；</li>\n"
        "<li>健康养生：柿饼营养价值与食用宜忌；</li>\n"
        "<li>美食食谱：柿饼的花样吃法与挑选保存技巧；</li>\n"
        "<li>柿饼知识：工艺、柿霜等冷知识科普。</li>\n"
        "</ul>\n"
        '<h2 id="domains">域名出售与出租</h2>\n'
        "<p>本站运营方持有多个柿饼行业精品中文域名，现面向柿饼产区商家、合作社、电商店铺与品牌方出售或出租。中文域名直指行业、便于记忆与传播，是搭建产地直供、品牌官网与电商站点的天然入口。</p>\n"
        "<ul>\n"
        + "".join("<li>" + esc(d) + "（" + puny(d) + "）</li>\n" for d in SALE_DOMAINS)
        + "</ul>\n"
        "<p>合作方式：可一次性购买转让，也可按年出租。价格与合作细节请联系：<a href=\"mailto:" + CONTACT_EMAIL + "\">" + CONTACT_EMAIL + "</a>。</p>\n"
        '<h2 id="contact">投稿与合作</h2>\n'
        "<p>欢迎柿饼产区商家、合作社、行业从业者与我们交流分享、投稿合作，联系邮箱：<a href=\"mailto:" + CONTACT_EMAIL + "\">" + CONTACT_EMAIL + "</a>。</p>\n"
        '<h2 id="statement">免责声明</h2>\n'
        "<p>本站内容均为一般性资讯与知识科普，仅供读者参考，不构成医疗、投资或商业决策建议；文中价格与行情信息会随市场变化，请以实际为准。本站图片为AI生成原创素材。</p>\n"
        "</div></div></section>\n"
    )
    page = (
        head("关于本站｜" + SITE_NAME + "｜柿饼行业域名出售出租",
             "关于柿饼资讯网：柿饼.cn、柿饼.中国、富平柿饼.cn 等柿饼行业中文域名出售出租，站点介绍、投稿合作与免责声明。",
             DOMAIN + "/about.html")
        + header_html("", "about.html")
        + "<main>" + body + "</main>\n"
        + footer_html("")
        + "</body>\n</html>\n"
    )
    return page


def render_404():
    body = (
        '<section class="err404">\n'
        '<div class="num">404</div>\n'
        "<h1>页面走丢了</h1>\n"
        "<p>您访问的页面可能已被移除或链接有误。</p>\n"
        '<a class="btn" href="index.html">返回首页</a>\n'
        "</section>\n"
    )
    page = (
        head("404｜" + SITE_NAME, "页面不存在，返回柿饼资讯网首页。", DOMAIN + "/404.html")
        + header_html("")
        + "<main>" + body + "</main>\n"
        + footer_html("")
        + "</body>\n</html>\n"
    )
    return page


def render_sitemap():
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    entries = [("", "index.html", "2026-10-21"), ("", "about.html", "2026-10-21")]
    for c in CATS:
        entries.append(("", "category-" + c + ".html", "2026-10-21"))
    for a in ARTICLES:
        entries.append(("news/", a["slug"] + ".html", a["date"]))
    for path, fn, lastmod in entries:
        lines.append("  <url>")
        lines.append("    <loc>" + DOMAIN + "/" + path + fn + "</loc>")
        lines.append("    <lastmod>" + lastmod + "</lastmod>")
        lines.append("    <changefreq>" + ("weekly" if path else "daily") + "</changefreq>")
        lines.append("  </url>")
    lines.append("</urlset>")
    return "\n".join(lines) + "\n"


def render_robots():
    return "User-agent: *\nAllow: /\n\nSitemap: " + DOMAIN + "/sitemap.xml\n"


# ---------------- 主流程 ----------------

def main():
    def w(name, content):
        with open(os.path.join(BASE, name), "w", encoding="utf-8", newline="\n") as f:
            f.write(content)
        print("written:", name)

    w("index.html", render_index())
    for c in CATS:
        w("category-" + c + ".html", render_category(c))
    for a in ARTICLES:
        w(os.path.join("news", a["slug"] + ".html"), render_article(a))
    w("about.html", render_about())
    w("404.html", render_404())
    w("sitemap.xml", render_sitemap())
    w("robots.txt", render_robots())
    print("done. total articles:", len(ARTICLES))


if __name__ == "__main__":
    main()
