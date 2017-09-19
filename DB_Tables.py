#在MySQL中运行，放在这里仅用于备忘

#房间表，存房间信息
create table rooms(
        id int primary key auto_increment,	#房间id，6位随机数字
        host nchar(30),						#房主OpenID
        num int,							#几人游戏，6-8
        state int,							#当前游戏进程：0等待人满，1选择颜色，2选择身份，
                                            #              3鉴定宝物，4使用技能，5传递顺位，6等待发言，7高票宝物，8低票宝物，9确定选择
                                            #              10-16重复第2轮
                                            #              17-23重复第3轮
                                            #              24判断结束，25鉴人回合，26终局信息
    	cur_player int,						#当前玩家，颜色编号，1-8
    	vp_atq int,							#鉴宝得分，0-6
    	vp_player int,						#鉴人得分，0-4
    	vp_total int,						#总得分，0-9 
        r1_a1 int,                          #第1轮票数最高的宝物，1-12
        r1_a2 int,                          #第1轮票数第2高的宝物，1-12
        r2_a1 int,
        r2_a2 int,
        r3_a1 int,
        r3_a2 int,
    	a1_rd int,							#宝物1是，1-12,1是鼠
    	a1_tf int,							#宝物1真假，0假1真
    	a1_state int,						#宝物1状态，0正常，1被老朝奉换，2被郑国渠盖
    	a2_rd int,
    	a2_tf int,
    	a2_state int,
    	a3_rd int,
    	a3_tf int,
    	a3_state int,
    	a4_rd int,
    	a4_tf int,
    	a4_state int,
    	a5_rd int,
    	a5_tf int,
    	a5_state int,
    	a6_rd int,
    	a6_tf int,
    	a6_state int,
    	a7_rd int,
    	a7_tf int,
    	a7_state int,
    	a8_rd int,
    	a8_tf int,
    	a8_state int,
    	a9_rd int,
    	a9_tf int,
    	a9_state int,
    	a10_rd int,
    	a10_tf int,
    	a10_state int,
    	a11_rd int,
    	a11_tf int,
    	a11_state int,
    	a12_rd int,
    	a12_tf int,
    	a12_state int
)

#玩家表，存玩家信息
create table players(
        id nchar(30) primary key,	#玩家OpenID
        room int,					#房间id，6位随机数字
		color int,					#颜色号，1-8，“1.红色，2.橙色，3.黄色，4.蓝色，5.绿色，6.紫色，7.黑色，8.白色”
    	role int,					#角色号，1-8，“1.许愿，2.方震，3.黄烟烟，4.木户加奈，5.老朝奉，6.药不然，7.郑国渠，8.姬云浮”
    	mate int,					#队友颜色号，1-8
    	flag int,					#本轮是否行动过，0-1，0未行动，1已行动
    	r1_state int,				#第1回合状态，0-2，0正常，1被药不然偷袭，2无法鉴定
    	r1_atq int,					#第1回合鉴定宝物，1-12
    	r1_atq_result int,			#第1回合鉴宝结果，0-3,0假，1真，2被药不然偷袭，3无法鉴定
    	r1_skill_obj int,			#第1回合技能对象，1-12，与角色号联合解析，0为未使用技能
    	r1_skill_result int,		#第1回合技能结果，0-3,与角色号联合解析，0假/坏人，1真/好人，2被药不然偷袭，3无法鉴定
    	r2_state int,
    	r2_atq int,
    	r2_atq_result int,
    	r2_skill_obj int,
    	r2_skill_result int,
    	r3_state int,
    	r3_atq int,
    	r3_atq_result int,
    	r3_skill_obj int,
    	r3_skill_result int,
    	player_obj int				#鉴人回合投票对象
)