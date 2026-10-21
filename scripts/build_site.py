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
        '<a href="' + prefix + 'about.html#contact">投稿与合作</a>'
        '<a href="' + prefix + 'about.html#statement">免责声明</a>'
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
        '<h2 id="contact">投稿与合作</h2>\n'
        "<p>欢迎柿饼产区商家、行业从业者与我们交流分享。投稿与合作联系邮箱暂未开通，请通过站点留言或后续公布的渠道联系我们。</p>\n"
        '<h2 id="statement">免责声明</h2>\n'
        "<p>本站内容均为一般性资讯与知识科普，仅供读者参考，不构成医疗、投资或商业决策建议；文中价格与行情信息会随市场变化，请以实际为准。本站图片为AI生成原创素材。</p>\n"
        "</div></div></section>\n"
    )
    page = (
        head("关于本站｜" + SITE_NAME, "关于柿饼资讯网：站点定位、内容栏目、投稿合作与免责声明。", DOMAIN + "/about.html")
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
