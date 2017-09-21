# -*- coding: utf-8 -*-
import Mysql
import random

#老齐修改符，测试结束后搜索“老齐修改符”逐条修改

#流程控制函数
def Menu(db,command,user,switch):
    '主菜单函数，区分全局命令与流程命令'
    intcmd = 99
    if command.isdigit():
        intcmd = int(command)
    #if command == u"？" or command == "?" :
    if switch == 1:
        return Atq_Help(db,user)
    #elif command == u"，" or command == ",":
    elif switch == 2:
        return Atq_History(db,user)
    #elif command == u"！" or command == "!":
    elif switch == 3:
        return Atq_Start(db,user)
    elif switch == 4:
        return Atq_Exit(db,user)
    elif (0 <= intcmd <= 8) or (100000 <= intcmd <= 999999):
        return Atq_Menu(db,intcmd,user,0)
    else:
        return Atq_Menu(db,intcmd,user,1)
    
def Atq_Help(db,user):
    return u"感谢查看，更多帮助信息请查看游戏挡板内侧说明"

def Atq_History(db,user):
    '历史记录函数'
    this_player = list(db.select('players' , where="id = \'"+user+"\'"))
    if not this_player:
        return u"你尚未开始游戏，无法查看历史记录！"
    else:
        room_id = this_player[0]["room"]
        color = this_player[0]["color"]
        role = this_player[0]["role"]
        mate = this_player[0]["mate"]
        flag = this_player[0]["flag"]
        r1 = this_player[0]["r1_atq"]
        r2 = this_player[0]["r2_atq"]
        r3 = this_player[0]["r3_atq"]
        k1 = this_player[0]["r1_skill_obj"]
        kr1 = this_player[0]["r1_skill_result"]
        k2 = this_player[0]["r2_skill_obj"]
        kr2 = this_player[0]["r2_skill_result"]
        k3 = this_player[0]["r3_skill_obj"]
        kr3 = this_player[0]["r3_skill_result"]
        history_text = u""
        if not color:
            history_text = history_text+u"你尚未选择颜色！"
        else:
            history_text = history_text+u"你是"+atq_color(color)+u"玩家"
        if not role:
            history_text = history_text+u"\n你尚未选择角色！\n"
        else:
            history_text = history_text+atq_role(role)+u"\n"
        if mate:
            history_text = history_text+u"你的队友是"+atq_color(mate)+u"玩家\n"
        if flag:
            history_text = history_text+u"你当前轮已行动\n"
        else:
            history_text = history_text+u"你当前轮行动未完成\n"
        if r1:
            history_text = history_text+u"你第1轮鉴定的"+atq_atq(r1)+u"："+atq_tf(this_player[0]["r1_atq_result"])+u"\n"
        if k1 != 99:
            if role == 3:
                pass
            elif role == 4:
                pass
            elif role == 8:
                pass
            elif role == 5:
                if k1==0 :
                    history_text = history_text+u"你第1轮未使用技能\n"
                else:
                    history_text = history_text+u"你第1轮成功使用技能\n"
            elif this_player[0]["role"] == 1:
                history_text = history_text+u"你第1轮额外鉴定的"+atq_atq(k1)+u"："+atq_tf(kr1)+u"\n"
            elif this_player[0]["role"] == 7:
                if k1==0 :
                    history_text = history_text+u"你第1轮未使用技能\n"
                else:
                    history_text = history_text+u"你第1轮成功使用技能，隐藏了"+atq_atq(k1)+u"\n"
            elif this_player[0]["role"] == 2:
                history_text = history_text+u"你第1轮查验的"+atq_color(k1)+u"玩家："+atq_ptf(kr1)+u"\n"
            elif this_player[0]["role"] == 6:
                if k1==0 :
                    history_text = history_text+u"你第1轮未使用技能\n"
                else:
                    history_text = history_text+u"你第1轮偷袭了"+atq_color(k1)+u"玩家\n"
            else:
                pass
        if r2:
            history_text = history_text+u"你第2轮鉴定的"+atq_atq(r2)+u"："+atq_tf(this_player[0]["r2_atq_result"])+u"\n"
        if k2 != 99:
            if role == 3:
                pass
            elif role == 4:
                pass
            elif role == 8:
                pass
            elif role == 5:
                if k2==0 :
                    history_text = history_text+u"你第2轮未使用技能\n"
                else:
                    history_text = history_text+u"你第2轮成功使用技能\n"
            elif this_player[0]["role"] == 1:
                history_text = history_text+u"你第2轮额外鉴定的"+atq_atq(k2)+u"："+atq_tf(kr2)+u"\n"
            elif this_player[0]["role"] == 7:
                if k2==0 :
                    history_text = history_text+u"你第2轮未使用技能\n"
                else:
                    history_text = history_text+u"你第2轮成功使用技能，隐藏了"+atq_atq(k2)+u"\n"
            elif this_player[0]["role"] == 2:
                history_text = history_text+u"你第2轮查验的"+atq_color(k2)+u"玩家："+atq_ptf(kr2)+u"\n"
            elif this_player[0]["role"] == 6:
                if k2==0 :
                    history_text = history_text+u"你第2轮未使用技能\n"
                else:
                    history_text = history_text+u"你第2轮偷袭了"+atq_color(k1)+u"玩家\n"
            else:
                pass   
        if r3:
            history_text = history_text+u"你第3轮鉴定的"+atq_atq(r3)+u"："+atq_tf(this_player[0]["r3_atq_result"])+u"\n"
        if k3 != 99:
            if role == 3:
                pass
            elif role == 4:
                pass
            elif role == 8:
                pass
            elif role == 5:
                if k3==0 :
                    history_text = history_text+u"你第3轮未使用技能\n"
                else:
                    history_text = history_text+u"你第3轮成功使用技能\n"
            elif this_player[0]["role"] == 1:
                history_text = history_text+u"你第2轮额外鉴定的"+atq_atq(k3)+u"："+atq_tf(kr3)+u"\n"
            elif this_player[0]["role"] == 7:
                if k3==0 :
                    history_text = history_text+u"你第3轮未使用技能\n"
                else:
                    history_text = history_text+u"你第3轮成功使用技能，隐藏了"+atq_atq(k3)+u"\n"
            elif this_player[0]["role"] == 2:
                history_text = history_text+u"你第3轮查验的"+atq_color(k3)+u"玩家："+atq_ptf(kr3)+u"\n"
            elif this_player[0]["role"] == 6:
                if k3==0 :
                    history_text = history_text+u"你第3轮未使用技能\n"
                else:
                    history_text = history_text+u"你第3轮偷袭了"+atq_color(k1)+u"玩家\n"
            else:
                pass     
    return history_text

def Atq_Start(db,user):
    '开始游戏函数'
    results = list(db.select('players' , where="id = \'"+user+"\'"))
    if not results:
        return u"欢迎使用古董局中局鉴宝助手！\n请按以下提示输入命令操作：\n 创建房间：游戏人数（6-8）\n 加入房间：6位房间号"
    else:
        return u"你已在游戏中！"

def Atq_Exit(db,user):
    '退出房间函数'
    results = list(db.select('players' , where="id = \'"+user+"\'"))
    if not results:
        return u"你未在房间中，无法退出房间！"
    else:
        room_id = results[0]["room"]
        host_id = list(db.select('rooms' , where="id = "+str(room_id)+""))[0]["host"]
        game_state = list(db.select('rooms' , where="id = "+str(room_id)+""))[0]["state"]
        if user == host_id:
            #房主整房退出
            num_delete = db.delete('players', where="room = \'"+str(room_id)+"\'")
            db.delete('rooms', where="id = \'"+str(room_id)+"\'")
            return u"你是房间："+str(room_id)+u"的房主，房间内所有"+str(num_delete)+u"名玩家均已成功退出房间"
        elif game_state == 0 or game_state == 26:
            #开局前或结束后访客自己退出
            db.delete('players', where="id = \'"+user+"\'")
            return u"退出房间："+str(room_id)+u"成功！"
        else:
            return u"退出房间："+str(room_id)+u"失败，游戏已经开始，只有房主才能退出房间"

def Atq_Menu(db,intcmd,user,flag):
    '流程命令模块，flag为1时只打印提示，flag为0时才执行操作'
    help_text = u""
    this_player = list(db.select('players' , where="id = \'"+user+"\'"))
    if not this_player:
        if flag:
            return u"欢迎使用古董局中局鉴宝助手！\n请按以下提示输入命令操作：\n 创建房间：游戏人数（6-8）\n 加入房间：6位房间号"+help_text
        elif 6 <= intcmd <= 8:
            return room_create(db,intcmd,user)
        elif 100000 <= intcmd <= 999999:
            return room_join(db,intcmd,user)
        else:
            return Atq_Menu(db,intcmd,user,1)
    else:
        room_id = this_player[0]["room"]
        res_room = list(db.select('rooms' , where="id = "+str(room_id)+""))
        res_players = list(db.select('players' , where="room = "+str(room_id)+""))
        host_id = res_room[0]["host"]
        num_room = res_room[0]["num"]
        num_players = len(res_players)
        game_state = res_room[0]["state"]
        cur_player = res_room[0]["cur_player"]
        #进入房间等待房主开始
        if game_state == 0:
            if flag:
                if host_id == user:
                    return u"请等待房间人满\n房间号："+str(room_id)+u"\n所需游戏人数："+str(num_room)+u"\n当前游戏人数："+str(num_players)+u"\n 开始游戏：0"+help_text
                else:
                    return u"请等待房间人满后房主输入0开始游戏\n房间号："+str(room_id)+u"\n所需游戏人数："+str(num_room)+u"\n当前游戏人数："+str(num_players)+help_text
            #老齐修改符，测试完成后改成下面的一行判断
            elif host_id == user and intcmd == 0 :
            #elif host_id == user and intcmd == 0 and num_players >= num_room:
                #更新房间状态
                db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                return u"开始游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
            else:
                return Atq_Menu(db,intcmd,user,1)
        #选择颜色    
        elif game_state == 1:
            if flag:
                if not this_player[0]["color"]:
                    return u"请按要求输入自己的颜色，所有玩家输入完成后，房主输入0继续游戏\n 选择红色：1\n 选择橙色：2\n 选择黄色：3\n 选择蓝色：4\n 选择绿色：5\n 选择紫色：6\n 选择黑色：7\n 选择白色：8"+help_text
                elif host_id == user:
                    return u"你已选择："+atq_color(this_player[0]["color"])+u"，可以输入对应编号更改颜色\n请等待所有玩家完成选择\n 继续游戏：0"+help_text
                else:
                    return u"你已选择："+atq_color(this_player[0]["color"])+u"，可以输入对应编号更改颜色\n所有玩家输入完成后，房主输入0继续游戏"+help_text    
            elif 1 <= intcmd <= 8:
                db.update('players',  where="id = \'"+user+"\'", color = intcmd )
                return u"选择"+atq_color(intcmd)+u"成功！\n"+Atq_Menu(db,intcmd,user,1)
            elif host_id == user and intcmd == 0:
                check_color = 0
                color_list = []
                for player in res_players:
                    if player["color"] == 0:
                        check_color = 1 
                    color_list.append(player["color"])
                if len(color_list)!=len(set(color_list)):
                    check_color = 1
                if check_color:
                    return u"有玩家尚未选择或选择了相同的颜色，请选错的玩家重新选择！\n"+Atq_Menu(db,intcmd,user,1)
                else:
                    #更新房间状态，并设置起始玩家
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,cur_player = random.choice(color_list) )
                    return u"颜色选择完成！\n"+Atq_Menu(db,intcmd,user,1)
            else:
                return Atq_Menu(db,intcmd,user,1)
        #选择身份
        elif game_state == 2:
            if flag:
                pro_text = u"所有玩家输入完成后，房主输入0继续游戏"
                for role in range(num_room):
                    pro_text = pro_text + u"\n 选择"+atq_role(role+1)+u"："+str(role+1)
                pro_text = pro_text + u"\n 继续游戏：0【房主操作】"    
                if not this_player[0]["role"]:
                    return u"请按要求输入自己的角色，"+pro_text + help_text
                elif host_id == user:
                    return u"你已选择："+atq_role(this_player[0]["role"])+u"，可以输入对应编号更改角色\n请等待所有玩家完成选择\n 继续游戏：0"+help_text
                else:
                    return u"你已选择："+atq_role(this_player[0]["role"])+u"，可以输入对应编号更改角色\n所有玩家输入完成后，房主输入0继续游戏"+help_text
            elif 1 <= intcmd <= num_room:
                db.update('players',  where="id = \'"+user+"\'", role = intcmd )
                return u"选择"+atq_role(intcmd)+u"成功！\n"+Atq_Menu(db,intcmd,user,1)
            elif num_room < intcmd <= 8:
                return u"当前游戏位"+str(num)+u"人局，"+u"无法选择"+atq_role(intcmd)+u"！\n"+Atq_Menu(db,intcmd,user,1)
            elif host_id == user and intcmd == 0:
                check_role = 0
                role_list = []
                for player in res_players:
                    if player["role"] == 0:
                        check_role = 1 
                    role_list.append(player["role"])
                if len(role_list)!=len(set(role_list)):
                    check_role = 1
                if check_role:
                    return u"有玩家尚未选择或选择了相同的角色，请选错的玩家重新选择！\n"+Atq_Menu(db,intcmd,user,1)
                else:
                    #处理老朝奉和药不然互认身份
                    #处理黄烟烟和木户加奈随机回合，方震3回合无法鉴定
                    id_fz = id_hyy = id_mhjn = id_lcf = id_ybr =""
                    color_lcf = color_ybr = 0
                    for player in res_players:
                        if player["role"] == 2:
                            id_fz = player["id"]
                        elif player["role"] == 3:
                            id_hyy = player["id"]  
                        elif player["role"] == 4:
                            id_mhjn = player["id"]
                        elif player["role"] == 5:
                            id_lcf = player["id"]
                            color_lcf = player["color"]
                        elif player["role"] == 6:
                            id_ybr = player["id"]
                            color_ybr = player["color"]       
                    atq_hyy=[0,0,2]
                    atq_mhjn=[0,0,2]
                    random.shuffle(atq_hyy)
                    random.shuffle(atq_mhjn)
                    if id_fz:
                        db.update('players',  where="id = \'"+id_fz+"\'", r1_state = 2, r2_state = 2, r3_state = 2 )
                    if id_hyy:
                        db.update('players',  where="id = \'"+id_hyy+"\'", r1_state = atq_hyy[0], r2_state = atq_hyy[1], r3_state = atq_hyy[2] )
                    if id_mhjn:
                        db.update('players',  where="id = \'"+id_mhjn+"\'", r1_state = atq_mhjn[0], r2_state = atq_mhjn[1], r3_state = atq_mhjn[2] )
                    if id_lcf:
                        db.update('players',  where="id = \'"+id_lcf+"\'", mate = color_ybr)
                    if id_ybr:
                        db.update('players',  where="id = \'"+id_ybr+"\'", mate = color_lcf)   
                    #更新房间状态
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                    return u"角色选择完成！\n"+Atq_Menu(db,intcmd,user,1)
            else:
                return Atq_Menu(db,intcmd,user,1)
        
        #---------第1轮----------------------------------------------------------------------------------------------------------------
        #第1轮鉴宝    
        elif 3<= game_state <=5 :
            atq = [
                    [ res_room[0]["a1_rd"],res_room[0]["a1_tf"],res_room[0]["a1_state"]],
                    [ res_room[0]["a2_rd"],res_room[0]["a2_tf"],res_room[0]["a2_state"]],
                    [ res_room[0]["a3_rd"],res_room[0]["a3_tf"],res_room[0]["a3_state"]],
                    [ res_room[0]["a4_rd"],res_room[0]["a4_tf"],res_room[0]["a4_state"]],
                  ]
            if flag:
                if this_player[0]["color"] != cur_player:
                    return u"当前玩家为"+atq_color(cur_player)+u"玩家，请等待他完成操作\n第1轮宝物为："+atq_atq(atq[0][0])+u"、"+atq_atq(atq[1][0])+u"、"+atq_atq(atq[2][0])+u"、"+atq_atq(atq[3][0])+help_text
                elif game_state == 3:
                    return u"请按下列提示鉴定第1轮宝物：\n 鉴定"+atq_atq(atq[0][0])+u"：1\n 鉴定"+atq_atq(atq[1][0])+u"：2\n 鉴定"+atq_atq(atq[2][0])+u"：3\n 鉴定"+atq_atq(atq[3][0])+u"：4"+help_text
                #技能提示信息
                elif game_state == 4:
                    if this_player[0]["r1_state"] == 1:
                        return u"你被药不然偷袭了，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 3:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，无主动技能，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 4:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，无主动技能，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 8:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，无主动技能，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 5:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择是否使用技能\n 使用技能：1\n 不用技能：0"+help_text
                    elif this_player[0]["role"] == 1:
                        #过滤已鉴定宝物信息
                        for num in range(4):
                            if atq[num][0] == this_player[0]["r1_atq"]:
                                del atq[num]
                                break
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择额外鉴定的宝物\n 鉴定"+atq_atq(atq[0][0])+u"：1\n 鉴定"+atq_atq(atq[1][0])+u"：2\n 鉴定"+atq_atq(atq[2][0])+u"：3\n"+help_text
                    elif this_player[0]["role"] == 7:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择隐藏的宝物\n 隐藏"+atq_atq(atq[0][0])+u"：1\n 隐藏"+atq_atq(atq[1][0])+u"：2\n 隐藏"+atq_atq(atq[2][0])+u"：3\n 隐藏"+atq_atq(atq[3][0])+u"：4\n 不用技能：0"+help_text
                    elif this_player[0]["role"] == 2:
                        pro_text = u""
                        player_list = []
                        for player in res_players:
                            if player["role"] != 2:
                                pro_text = pro_text + u" \n查验" + atq_color(player["color"]) + u"玩家："+str(player["color"])
                                player_list.append(player["color"])
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择你要查验阵营的玩家颜色"+ pro_text + help_text
                    elif this_player[0]["role"] == 6:
                        pro_text = u""
                        player_list = []
                        for player in res_players:
                            if player["role"] != 6:
                                pro_text = pro_text + u" \n偷袭" + atq_color(player["color"]) + u"玩家："+str(player["color"])
                                player_list.append(player["color"])
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择你要偷袭的玩家颜色"+ pro_text + u"\n 不用技能：0" + help_text
                    else:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，未知技能"+help_text
                elif game_state == 5:
                    pro_text = u""
                    player_list = []
                    for player in res_players:
                        if not player["flag"]:
                            pro_text = pro_text + u" \n选择" + atq_color(player["color"]) + u"玩家："+str(player["color"])
                            player_list.append(player["color"])
                    if player_list:
                        return u"请从以下本轮未行动的玩家中选择1名继续行动"+pro_text +help_text
                    else:
                        return u"你已经是本轮最后1位玩家，请输入0继续游戏\n 继续游戏：0"+help_text
            #--------------------------------------鉴宝处理----------------------------------------    
            elif (this_player[0]["color"] == cur_player) and game_state==3 and (1<=intcmd<=4):
                #你被药不然偷袭了
                if this_player[0]["r1_state"] == 1:
                    db.update('players',  where="id = \'"+user+"\'", r1_atq = atq[intcmd-1][0] , r1_atq_result = 2)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你被药不然偷袭了，无法鉴定宝物！\n"+Atq_Menu(db,intcmd,user,1)
                #自身无法鉴定或宝物无法被鉴定
                elif this_player[0]["r1_state"] == 2 or atq[intcmd-1][2] == 2:
                    db.update('players',  where="id = \'"+user+"\'", r1_atq = atq[intcmd-1][0], r1_atq_result = 3)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你无法鉴定这件宝物的真假！\n"+Atq_Menu(db,intcmd,user,1)
                #老朝奉换过且你是姬云浮以外的好人
                elif this_player[0]["role"] <= 4 and atq[intcmd-1][2] == 1:
                    tf_flag = 1 - atq[intcmd-1][1]
                    db.update('players',  where="id = \'"+user+"\'", r1_atq = atq[intcmd-1][0], r1_atq_result = tf_flag)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你本回合鉴定的"+atq_atq(atq[intcmd-1][0])+u"是"+atq_tf(tf_flag)+u"\n"+Atq_Menu(db,intcmd,user,1)
                #直接赋值宝物的真假
                else:
                    db.update('players',  where="id = \'"+user+"\'", r1_atq = atq[intcmd-1][0], r1_atq_result = atq[intcmd-1][1])
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你本回合鉴定的"+atq_atq(atq[intcmd-1][0])+u"是"+atq_tf(atq[intcmd-1][1])+u"\n"+Atq_Menu(db,intcmd,user,1)
            #--------------------------------------技能处理----------------------------------------       
            elif (this_player[0]["color"] == cur_player) and game_state==4 and (0<=intcmd<=8):
                #被药不然偷袭
                if this_player[0]["r1_state"] == 1:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                #黄烟烟
                elif this_player[0]["role"] == 3:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #木户加奈
                elif this_player[0]["role"] == 4:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #姬云浮
                elif this_player[0]["role"] == 8:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #老朝奉
                elif this_player[0]["role"] == 5:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r1_skill_obj = 0)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你未使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    elif intcmd == 1:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r1_skill_obj = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,a1_state = 1 ,a2_state = 1 ,a3_state = 1 ,a4_state = 1 )
                        return u"你已成功使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #许愿
                elif this_player[0]["role"] == 1:
                    if 1<= intcmd <= 3:
                        for num in range(4):
                            if atq[num][0] == this_player[0]["r1_atq"]:
                                del atq[num]
                                break
                        tf_flag = atq[intcmd-1][1]        
                        if atq[intcmd-1][2] == 1:
                            tf_flag = 1 - tf_flag
                        elif atq[intcmd-1][2] == 2:
                            tf_flag = 3
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r1_skill_obj = atq[intcmd-1][0], r1_skill_result = tf_flag )
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你本回合额外鉴定了"+atq_atq(atq[intcmd-1][0])+u"，结果是："+atq_tf(tf_flag)+u"\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #郑国渠
                elif this_player[0]["role"] == 7:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r1_skill_obj = 0)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你未使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    elif 1<= intcmd <= 4:
                        atq[intcmd-1][2] = 2
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r1_skill_obj = atq[intcmd-1][0])
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,a1_state = atq[0][2] ,a2_state = atq[1][2] ,a3_state = atq[2][2] ,a4_state = atq[3][2])
                        return u"你已成功使用技能，隐藏了"+atq_atq(atq[intcmd-1][0])+u"\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #方震
                elif this_player[0]["role"] == 2:
                    player_list = []
                    role_list = []
                    for player in res_players:
                        if player["role"] != 2:
                            role_list.append(player["role"])
                            player_list.append(player["color"])
                    if (intcmd in player_list):
                        obj_role = role_list[player_list.index(intcmd)]
                        if 1<= obj_role <=4 or obj_role == 8:
                            tf_flag = 1
                        elif 5 <= obj_role <= 7:
                            tf_flag = 0
                        #未知错误    
                        else:
                            tf_flag = 98
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r1_skill_obj = intcmd, r1_skill_result = tf_flag )
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )    
                        return u"你本回合查验了"+atq_color(intcmd)+u"玩家，结果是："+atq_ptf(tf_flag)+u"\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #药不然    
                elif this_player[0]["role"] == 6:
                    player_list = []
                    role_list = []
                    for player in res_players:
                        if player["role"] != 6:
                            role_list.append(player["role"])
                            player_list.append(player["color"])
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r1_skill_obj = 0)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你未使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    elif (intcmd in player_list):
                        #改变其他人玩家表
                        atq_attack(db,intcmd,user,1)
                        #改变自己玩家表和房间表
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r1_skill_obj = intcmd)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你本回合偷袭了"+atq_color(intcmd)+u"玩家\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                else:
                    db.update('players',  where="id = \'"+user+"\'", flag = 1)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                    return u"你是"+atq_role(this_player[0]["role"])+u"，未知技能"+help_text+u"\n"+Atq_Menu(db,intcmd,user,1)
            #--------------------------------------传位处理----------------------------------------       
            elif (this_player[0]["color"] == cur_player) and game_state==5 and (0<=intcmd<=8):
                player_list = []
                for player in res_players:
                    if not player["flag"]:
                        player_list.append(player["color"])
                if player_list:
                    if(intcmd in player_list):
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state - 2 ,cur_player = intcmd)
                        return u"你已经成功传给了"+atq_color(intcmd)+u"玩家\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1) 
                elif intcmd == 0:
                    db.update('players',  where="room = "+str(room_id)+"", flag = 0)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你已经成功继续游戏\n"+Atq_Menu(db,intcmd,user,1)
                else:
                    return Atq_Menu(db,intcmd,user,1) 
            else:
                return Atq_Menu(db,intcmd,user,1)
        #第1轮等待发言    
        elif game_state == 6:
            if flag:
                if host_id == user:
                    return u"发言阶段，请等待发言阶段结束\n 继续游戏：0"+help_text
                else:
                    return u"进入发言阶段，发言阶段结束后，房主输入0继续游戏"+help_text
            elif host_id == user and intcmd == 0 :
                #更新房间状态
                db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
            else:
                return Atq_Menu(db,intcmd,user,1)
        #第1轮录入鉴宝结果    
        elif 7 <= game_state <= 9 :
            atq = [
                    [ res_room[0]["a1_rd"],res_room[0]["a1_tf"]],
                    [ res_room[0]["a2_rd"],res_room[0]["a2_tf"]],
                    [ res_room[0]["a3_rd"],res_room[0]["a3_tf"]],
                    [ res_room[0]["a4_rd"],res_room[0]["a4_tf"]],
                  ]
            voted_atq = [res_room[0]["r1_a1"],res_room[0]["r1_a2"]]
            vp_atq = res_room[0]["vp_atq"]
            if flag:
                if user != host_id:
                    return u"房主正在录入鉴宝结果，请等待他完成操作！\n"+help_text
                elif game_state == 7:
                    return u"请按下列提示选择票数最高的宝物：\n "+atq_atq(atq[0][0])+u"：1\n "+atq_atq(atq[1][0])+u"：2\n "+atq_atq(atq[2][0])+u"：3\n "+atq_atq(atq[3][0])+u"：4"+help_text
                elif game_state == 8:
                    #过滤已鉴定宝物信息
                    for num in range(4):
                        if atq[num][0] == voted_atq[0]:
                            del atq[num]
                            break
                    return u"本轮票数最高的宝物为："+atq_atq(voted_atq[0])+u"\n请按下列提示选择票数第2高的宝物：\n "+atq_atq(atq[0][0])+u"：1\n "+atq_atq(atq[1][0])+u"：2\n "+atq_atq(atq[2][0])+u"：3\n "+help_text
                elif game_state == 9:
                    return u"本轮票数最高的宝物为："+atq_atq(voted_atq[0])+u"\n本轮票数第2高的宝物为："+atq_atq(voted_atq[1])+u"\n 继续游戏：0\n 重新选择：1"+help_text
                else:
                    return u"房间状态号越界"
            else:
                if user != host_id:
                    return Atq_Menu(db,intcmd,user,1) 
                elif game_state == 7 and 1<= intcmd <= 4:
                    voted_atq[0] = atq[intcmd-1][0]
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,r1_a1 = voted_atq[0], r1_a2 = voted_atq[1])
                    return u"选择"+atq_atq(voted_atq[0])+u"成功！\n "+Atq_Menu(db,intcmd,user,1) 
                elif game_state == 8 and 1<= intcmd <= 3:
                    for num in range(4):
                        if atq[num][0] == voted_atq[0]:
                            del atq[num]
                            break
                    voted_atq[1] = atq[intcmd-1][0]
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,r1_a1 = voted_atq[0], r1_a2 = voted_atq[1])
                    return u"选择"+atq_atq(voted_atq[1])+u"成功！\n "+Atq_Menu(db,intcmd,user,1)
                elif game_state == 9 and 0<= intcmd <= 1:
                    if intcmd == 1:
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state - 2 ,r1_a1 = 0, r1_a2 = 0)
                        return u"取消成功！请重新选择宝物\n"+Atq_Menu(db,intcmd,user,1)
                    elif intcmd ==0:
                        voted_tf = 0
                        for num in range(4):
                            if atq[num][0] == voted_atq[0]:
                                if atq[num][1] == 1:
                                    vp_atq += 1
                            if atq[num][0] == voted_atq[1]:
                                voted_tf  = atq[num][1]
                                if atq[num][1] == 1:
                                    vp_atq += 1
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,vp_atq = vp_atq)
                        return u"本轮票数最高的宝物为"+atq_atq(voted_atq[0])+u"：不公布真赝\n本轮票数第2高的宝物为"+atq_atq(voted_atq[1])+u"："+atq_tf(voted_tf)+u"\n\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return u"选择越界"
                else:
                    return Atq_Menu(db,intcmd,user,1)
        #---------第1轮结束----------------------------------------------------------------------------------------------------------------
        
        #---------第2轮----------------------------------------------------------------------------------------------------------------
        #第2轮鉴宝    
        elif 10<= game_state <=12 :
            atq = [
                    [ res_room[0]["a5_rd"],res_room[0]["a5_tf"],res_room[0]["a5_state"]],
                    [ res_room[0]["a6_rd"],res_room[0]["a6_tf"],res_room[0]["a6_state"]],
                    [ res_room[0]["a7_rd"],res_room[0]["a7_tf"],res_room[0]["a7_state"]],
                    [ res_room[0]["a8_rd"],res_room[0]["a8_tf"],res_room[0]["a8_state"]],
                  ]
            if flag:
                if this_player[0]["color"] != cur_player:
                    return u"当前玩家为"+atq_color(cur_player)+u"玩家，请等待他完成操作\n第2轮宝物为："+atq_atq(atq[0][0])+u"、"+atq_atq(atq[1][0])+u"、"+atq_atq(atq[2][0])+u"、"+atq_atq(atq[3][0])+help_text
                elif game_state == 10:
                    return u"请按下列提示鉴定第2轮宝物：\n 鉴定"+atq_atq(atq[0][0])+u"：1\n 鉴定"+atq_atq(atq[1][0])+u"：2\n 鉴定"+atq_atq(atq[2][0])+u"：3\n 鉴定"+atq_atq(atq[3][0])+u"：4"+help_text
                #技能提示信息
                elif game_state == 11:
                    if this_player[0]["r2_state"] == 1:
                        return u"你被药不然偷袭了，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 3:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，无主动技能，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 4:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，无主动技能，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 8:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，无主动技能，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 5:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择是否使用技能\n 使用技能：1\n 不用技能：0"+help_text
                    elif this_player[0]["role"] == 1:
                        #过滤已鉴定宝物信息
                        for num in range(4):
                            if atq[num][0] == this_player[0]["r2_atq"]:
                                del atq[num]
                                break
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择额外鉴定的宝物\n 鉴定"+atq_atq(atq[0][0])+u"：1\n 鉴定"+atq_atq(atq[1][0])+u"：2\n 鉴定"+atq_atq(atq[2][0])+u"：3\n"+help_text
                    elif this_player[0]["role"] == 7:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择隐藏的宝物\n 隐藏"+atq_atq(atq[0][0])+u"：1\n 隐藏"+atq_atq(atq[1][0])+u"：2\n 隐藏"+atq_atq(atq[2][0])+u"：3\n 隐藏"+atq_atq(atq[3][0])+u"：4\n 不用技能：0"+help_text
                    elif this_player[0]["role"] == 2:
                        pro_text = u""
                        player_list = []
                        for player in res_players:
                            if player["role"] != 2:
                                pro_text = pro_text + u" \n查验" + atq_color(player["color"]) + u"玩家："+str(player["color"])
                                player_list.append(player["color"])
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择你要查验阵营的玩家颜色"+ pro_text + help_text
                    elif this_player[0]["role"] == 6:
                        pro_text = u""
                        player_list = []
                        for player in res_players:
                            if player["role"] != 6:
                                pro_text = pro_text + u" \n偷袭" + atq_color(player["color"]) + u"玩家："+str(player["color"])
                                player_list.append(player["color"])
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择你要偷袭的玩家颜色"+ pro_text + u"\n 不用技能：0" + help_text
                    else:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，未知技能"+help_text
                elif game_state == 12:
                    pro_text = u""
                    player_list = []
                    for player in res_players:
                        if not player["flag"]:
                            pro_text = pro_text + u" \n选择" + atq_color(player["color"]) + u"玩家："+str(player["color"])
                            player_list.append(player["color"])
                    if player_list:
                        return u"请从以下本轮未行动的玩家中选择1名继续行动"+pro_text +help_text
                    else:
                        return u"你已经是本轮最后1位玩家，请输入0继续游戏\n 继续游戏：0"+help_text
            #--------------------------------------鉴宝处理----------------------------------------    
            elif (this_player[0]["color"] == cur_player) and game_state==10 and (1<=intcmd<=4):
                #你被药不然偷袭了
                if this_player[0]["r2_state"] == 1:
                    db.update('players',  where="id = \'"+user+"\'", r2_atq = atq[intcmd-1][0] , r2_atq_result = 2)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你被药不然偷袭了，无法鉴定宝物！\n"+Atq_Menu(db,intcmd,user,1)
                #自身无法鉴定或宝物无法被鉴定
                elif this_player[0]["r2_state"] == 2 or atq[intcmd-1][2] == 2:
                    db.update('players',  where="id = \'"+user+"\'", r2_atq = atq[intcmd-1][0], r2_atq_result = 3)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你无法鉴定这件宝物的真假！\n"+Atq_Menu(db,intcmd,user,1)
                #老朝奉换过且你是姬云浮以外的好人
                elif this_player[0]["role"] <= 4 and atq[intcmd-1][2] == 1:
                    tf_flag = 1 - atq[intcmd-1][1]
                    db.update('players',  where="id = \'"+user+"\'", r2_atq = atq[intcmd-1][0], r2_atq_result = tf_flag)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你本回合鉴定的"+atq_atq(atq[intcmd-1][0])+u"是"+atq_tf(tf_flag)+u"\n"+Atq_Menu(db,intcmd,user,1)
                #直接赋值宝物的真假
                else:
                    db.update('players',  where="id = \'"+user+"\'", r2_atq = atq[intcmd-1][0], r2_atq_result = atq[intcmd-1][1])
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你本回合鉴定的"+atq_atq(atq[intcmd-1][0])+u"是"+atq_tf(atq[intcmd-1][1])+u"\n"+Atq_Menu(db,intcmd,user,1)
            #--------------------------------------技能处理----------------------------------------       
            elif (this_player[0]["color"] == cur_player) and game_state==11 and (0<=intcmd<=8):
                #被药不然偷袭
                if this_player[0]["r2_state"] == 1:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                #黄烟烟
                elif this_player[0]["role"] == 3:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #木户加奈
                elif this_player[0]["role"] == 4:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #姬云浮
                elif this_player[0]["role"] == 8:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #老朝奉
                elif this_player[0]["role"] == 5:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r2_skill_obj = 0)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你未使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    elif intcmd == 1:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r2_skill_obj = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,a5_state = 1 ,a6_state = 1 ,a7_state = 1 ,a8_state = 1 )
                        return u"你已成功使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #许愿
                elif this_player[0]["role"] == 1:
                    if 1<= intcmd <= 3:
                        for num in range(4):
                            if atq[num][0] == this_player[0]["r2_atq"]:
                                del atq[num]
                                break
                        tf_flag = atq[intcmd-1][1]        
                        if atq[intcmd-1][2] == 1:
                            tf_flag = 1 - tf_flag
                        elif atq[intcmd-1][2] == 2:
                            tf_flag = 3
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r2_skill_obj = atq[intcmd-1][0], r2_skill_result = tf_flag )
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你本回合额外鉴定了"+atq_atq(atq[intcmd-1][0])+u"，结果是："+atq_tf(tf_flag)+u"\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #郑国渠
                elif this_player[0]["role"] == 7:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r2_skill_obj = 0)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你未使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    elif 1<= intcmd <= 4:
                        atq[intcmd-1][2] = 2
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r2_skill_obj = atq[intcmd-1][0])
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,a5_state = atq[0][2] ,a6_state = atq[1][2] ,a7_state = atq[2][2] ,a8_state = atq[3][2])
                        return u"你已成功使用技能，隐藏了"+atq_atq(atq[intcmd-1][0])+u"\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #方震
                elif this_player[0]["role"] == 2:
                    player_list = []
                    role_list = []
                    for player in res_players:
                        if player["role"] != 2:
                            role_list.append(player["role"])
                            player_list.append(player["color"])
                    if (intcmd in player_list):
                        obj_role = role_list[player_list.index(intcmd)]
                        if 1<= obj_role <=4 or obj_role == 8:
                            tf_flag = 1
                        elif 5 <= obj_role <= 7:
                            tf_flag = 0
                        #未知错误    
                        else:
                            tf_flag = 98
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r2_skill_obj = intcmd, r2_skill_result = tf_flag )
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )    
                        return u"你本回合查验了"+atq_color(intcmd)+u"玩家，结果是："+atq_ptf(tf_flag)+u"\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #药不然    
                elif this_player[0]["role"] == 6:
                    player_list = []
                    role_list = []
                    for player in res_players:
                        if player["role"] != 6:
                            role_list.append(player["role"])
                            player_list.append(player["color"])
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r2_skill_obj = 0)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你未使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    elif (intcmd in player_list):
                        #改变其他人玩家表
                        atq_attack(db,intcmd,user,2)
                        #改变自己玩家表和房间表
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r2_skill_obj = intcmd)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你本回合偷袭了"+atq_color(intcmd)+u"玩家\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                else:
                    db.update('players',  where="id = \'"+user+"\'", flag = 1)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                    return u"你是"+atq_role(this_player[0]["role"])+u"，未知技能"+help_text+u"\n"+Atq_Menu(db,intcmd,user,1)
            #--------------------------------------传位处理----------------------------------------       
            elif (this_player[0]["color"] == cur_player) and game_state==12 and (0<=intcmd<=8):
                player_list = []
                for player in res_players:
                    if not player["flag"]:
                        player_list.append(player["color"])
                if player_list:
                    if(intcmd in player_list):
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state - 2 ,cur_player = intcmd)
                        return u"你已经成功传给了"+atq_color(intcmd)+u"玩家\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1) 
                elif intcmd == 0:
                    db.update('players',  where="room = "+str(room_id)+"", flag = 0)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你已经成功继续游戏\n"+Atq_Menu(db,intcmd,user,1)
                else:
                    return Atq_Menu(db,intcmd,user,1) 
            else:
                return Atq_Menu(db,intcmd,user,1)
        #第2轮等待发言    
        elif game_state == 13:
            if flag:
                if host_id == user:
                    return u"发言阶段，请等待发言阶段结束\n 继续游戏：0"+help_text
                else:
                    return u"进入发言阶段，发言阶段结束后，房主输入0继续游戏"+help_text
            elif host_id == user and intcmd == 0:
                #更新房间状态
                db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
            else:
                return Atq_Menu(db,intcmd,user,1)
        #第2轮录入鉴宝结果    
        elif 14 <= game_state <= 16 :
            atq = [
                    [ res_room[0]["a5_rd"],res_room[0]["a5_tf"]],
                    [ res_room[0]["a6_rd"],res_room[0]["a6_tf"]],
                    [ res_room[0]["a7_rd"],res_room[0]["a7_tf"]],
                    [ res_room[0]["a8_rd"],res_room[0]["a8_tf"]],
                  ]
            vp_atq = res_room[0]["vp_atq"]         
            voted_atq = [res_room[0]["r2_a1"],res_room[0]["r2_a2"]]
            if flag:
                if user != host_id:
                    return u"房主正在录入鉴宝结果，请等待他完成操作！\n"+help_text
                elif game_state == 14:
                    return u"请按下列提示选择票数最高的宝物：\n "+atq_atq(atq[0][0])+u"：1\n "+atq_atq(atq[1][0])+u"：2\n "+atq_atq(atq[2][0])+u"：3\n "+atq_atq(atq[3][0])+u"：4"+help_text
                elif game_state == 15:
                    #过滤已鉴定宝物信息
                    for num in range(4):
                        if atq[num][0] == voted_atq[0]:
                            del atq[num]
                            break
                    return u"本轮票数最高的宝物为："+atq_atq(voted_atq[0])+u"\n请按下列提示选择票数第2高的宝物：\n "+atq_atq(atq[0][0])+u"：1\n "+atq_atq(atq[1][0])+u"：2\n "+atq_atq(atq[2][0])+u"：3\n "+help_text
                elif game_state == 16:
                    return u"本轮票数最高的宝物为："+atq_atq(voted_atq[0])+u"\n本轮票数第2高的宝物为："+atq_atq(voted_atq[1])+u"\n 继续游戏：0\n 重新选择：1"+help_text
                else:
                    return u"房间状态号越界"
            else:
                if user != host_id:
                    return Atq_Menu(db,intcmd,user,1) 
                elif game_state == 14 and 1<= intcmd <= 4:
                    voted_atq[0] = atq[intcmd-1][0]
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,r2_a1 = voted_atq[0], r2_a2 = voted_atq[1])
                    return u"选择"+atq_atq(voted_atq[0])+u"成功！\n "+Atq_Menu(db,intcmd,user,1) 
                elif game_state == 15 and 1<= intcmd <= 3:
                    for num in range(4):
                        if atq[num][0] == voted_atq[0]:
                            del atq[num]
                            break
                    voted_atq[1] = atq[intcmd-1][0]
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,r2_a1 = voted_atq[0], r2_a2 = voted_atq[1])
                    return u"选择"+atq_atq(voted_atq[1])+u"成功！\n "+Atq_Menu(db,intcmd,user,1)
                elif game_state == 16 and 0<= intcmd <= 1:
                    if intcmd == 1:
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state - 2 ,r2_a1 = 0, r2_a2 = 0)
                        return u"取消成功！请重新选择宝物\n"+Atq_Menu(db,intcmd,user,1)
                    elif intcmd ==0:
                        voted_tf = 0
                        for num in range(4):
                            if atq[num][0] == voted_atq[0]:
                                if atq[num][1] == 1:
                                    vp_atq += 1
                            if atq[num][0] == voted_atq[1]:
                                voted_tf  = atq[num][1]
                                if atq[num][1] == 1:
                                    vp_atq += 1
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,vp_atq = vp_atq)
                        return u"本轮票数最高的宝物为"+atq_atq(voted_atq[0])+u"：不公布真赝\n本轮票数第2高的宝物为"+atq_atq(voted_atq[1])+u"："+atq_tf(voted_tf)+u"\n\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return u"选择越界"
                else:
                    return Atq_Menu(db,intcmd,user,1)
        #---------第2轮结束----------------------------------------------------------------------------------------------------------------
        
        #---------第3轮----------------------------------------------------------------------------------------------------------------
        #第3轮鉴宝    
        elif 17<= game_state <=19 :
            atq = [
                    [ res_room[0]["a9_rd"],res_room[0]["a9_tf"],res_room[0]["a9_state"]],
                    [ res_room[0]["a10_rd"],res_room[0]["a10_tf"],res_room[0]["a10_state"]],
                    [ res_room[0]["a11_rd"],res_room[0]["a11_tf"],res_room[0]["a11_state"]],
                    [ res_room[0]["a12_rd"],res_room[0]["a12_tf"],res_room[0]["a12_state"]],
                  ]
            if flag:
                if this_player[0]["color"] != cur_player:
                    return u"当前玩家为"+atq_color(cur_player)+u"玩家，请等待他完成操作\n第3轮宝物为："+atq_atq(atq[0][0])+u"、"+atq_atq(atq[1][0])+u"、"+atq_atq(atq[2][0])+u"、"+atq_atq(atq[3][0])+help_text
                elif game_state == 17:
                    return u"请按下列提示鉴定第3轮宝物：\n 鉴定"+atq_atq(atq[0][0])+u"：1\n 鉴定"+atq_atq(atq[1][0])+u"：2\n 鉴定"+atq_atq(atq[2][0])+u"：3\n 鉴定"+atq_atq(atq[3][0])+u"：4"+help_text
                #技能提示信息
                elif game_state == 18:
                    if this_player[0]["r3_state"] == 1:
                        return u"你被药不然偷袭了，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 3:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，无主动技能，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 4:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，无主动技能，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 8:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，无主动技能，请输入0继续游戏\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 5:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择是否使用技能\n 使用技能：1\n 不用技能：0"+help_text
                    elif this_player[0]["role"] == 1:
                        #过滤已鉴定宝物信息
                        for num in range(4):
                            if atq[num][0] == this_player[0]["r3_atq"]:
                                del atq[num]
                                break
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择额外鉴定的宝物\n 鉴定"+atq_atq(atq[0][0])+u"：1\n 鉴定"+atq_atq(atq[1][0])+u"：2\n 鉴定"+atq_atq(atq[2][0])+u"：3\n"+help_text
                    elif this_player[0]["role"] == 7:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择隐藏的宝物\n 隐藏"+atq_atq(atq[0][0])+u"：1\n 隐藏"+atq_atq(atq[1][0])+u"：2\n 隐藏"+atq_atq(atq[2][0])+u"：3\n 隐藏"+atq_atq(atq[3][0])+u"：4\n 不用技能：0"+help_text
                    elif this_player[0]["role"] == 2:
                        pro_text = u""
                        player_list = []
                        for player in res_players:
                            if player["role"] != 2:
                                pro_text = pro_text + u" \n查验" + atq_color(player["color"]) + u"玩家："+str(player["color"])
                                player_list.append(player["color"])
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择你要查验阵营的玩家颜色"+ pro_text + help_text
                    elif this_player[0]["role"] == 6:
                        pro_text = u""
                        player_list = []
                        for player in res_players:
                            if player["role"] != 6:
                                pro_text = pro_text + u" \n偷袭" + atq_color(player["color"]) + u"玩家："+str(player["color"])
                                player_list.append(player["color"])
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按提示选择你要偷袭的玩家颜色"+ pro_text + u"\n 不用技能：0" + help_text
                    else:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，未知技能"+help_text
                elif game_state == 19:
                    pro_text = u""
                    player_list = []
                    for player in res_players:
                        if not player["flag"]:
                            pro_text = pro_text + u" \n选择" + atq_color(player["color"]) + u"玩家："+str(player["color"])
                            player_list.append(player["color"])
                    if player_list:
                        return u"请从以下本轮未行动的玩家中选择1名继续行动"+pro_text +help_text
                    else:
                        return u"你已经是本轮最后1位玩家，请输入0继续游戏\n 继续游戏：0"+help_text
            #--------------------------------------鉴宝处理----------------------------------------    
            elif (this_player[0]["color"] == cur_player) and game_state==17 and (1<=intcmd<=4):
                #你被药不然偷袭了
                if this_player[0]["r3_state"] == 1:
                    db.update('players',  where="id = \'"+user+"\'", r3_atq = atq[intcmd-1][0] , r3_atq_result = 2)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你被药不然偷袭了，无法鉴定宝物！\n"+Atq_Menu(db,intcmd,user,1)
                #自身无法鉴定或宝物无法被鉴定
                elif this_player[0]["r3_state"] == 2 or atq[intcmd-1][2] == 2:
                    db.update('players',  where="id = \'"+user+"\'", r3_atq = atq[intcmd-1][0], r3_atq_result = 3)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你无法鉴定这件宝物的真假！\n"+Atq_Menu(db,intcmd,user,1)
                #老朝奉换过且你是姬云浮以外的好人
                elif this_player[0]["role"] <= 4 and atq[intcmd-1][2] == 1:
                    tf_flag = 1 - atq[intcmd-1][1]
                    db.update('players',  where="id = \'"+user+"\'", r3_atq = atq[intcmd-1][0], r3_atq_result = tf_flag)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你本回合鉴定的"+atq_atq(atq[intcmd-1][0])+u"是"+atq_tf(tf_flag)+u"\n"+Atq_Menu(db,intcmd,user,1)
                #直接赋值宝物的真假
                else:
                    db.update('players',  where="id = \'"+user+"\'", r3_atq = atq[intcmd-1][0], r3_atq_result = atq[intcmd-1][1])
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你本回合鉴定的"+atq_atq(atq[intcmd-1][0])+u"是"+atq_tf(atq[intcmd-1][1])+u"\n"+Atq_Menu(db,intcmd,user,1)
            #--------------------------------------技能处理----------------------------------------       
            elif (this_player[0]["color"] == cur_player) and game_state==18 and (0<=intcmd<=8):
                #被药不然偷袭
                if this_player[0]["r3_state"] == 1:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                #黄烟烟
                elif this_player[0]["role"] == 3:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #木户加奈
                elif this_player[0]["role"] == 4:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #姬云浮
                elif this_player[0]["role"] == 8:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #老朝奉
                elif this_player[0]["role"] == 5:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r3_skill_obj = 0)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你未使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    elif intcmd == 1:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r3_skill_obj = 1)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,a9_state = 1 ,a10_state = 1 ,a11_state = 1 ,a12_state = 1 )
                        return u"你已成功使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #许愿
                elif this_player[0]["role"] == 1:
                    if 1<= intcmd <= 3:
                        for num in range(4):
                            if atq[num][0] == this_player[0]["r3_atq"]:
                                del atq[num]
                                break
                        tf_flag = atq[intcmd-1][1]        
                        if atq[intcmd-1][2] == 1:
                            tf_flag = 1 - tf_flag
                        elif atq[intcmd-1][2] == 2:
                            tf_flag = 3
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r3_skill_obj = atq[intcmd-1][0], r3_skill_result = tf_flag )
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你本回合额外鉴定了"+atq_atq(atq[intcmd-1][0])+u"，结果是："+atq_tf(tf_flag)+u"\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #郑国渠
                elif this_player[0]["role"] == 7:
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r3_skill_obj = 0)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你未使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    elif 1<= intcmd <= 4:
                        atq[intcmd-1][2] = 2
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r3_skill_obj = atq[intcmd-1][0])
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,a9_state = atq[0][2] ,a10_state = atq[1][2] ,a11_state = atq[2][2] ,a12_state = atq[3][2])
                        return u"你已成功使用技能，隐藏了"+atq_atq(atq[intcmd-1][0])+u"\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #方震
                elif this_player[0]["role"] == 2:
                    player_list = []
                    role_list = []
                    for player in res_players:
                        if player["role"] != 2:
                            role_list.append(player["role"])
                            player_list.append(player["color"])
                    if (intcmd in player_list):
                        obj_role = role_list[player_list.index(intcmd)]
                        if 1<= obj_role <=4 or obj_role == 8:
                            tf_flag = 1
                        elif 5 <= obj_role <= 7:
                            tf_flag = 0
                        #未知错误    
                        else:
                            tf_flag = 98
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r3_skill_obj = intcmd, r3_skill_result = tf_flag )
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )    
                        return u"你本回合查验了"+atq_color(intcmd)+u"玩家，结果是："+atq_ptf(tf_flag)+u"\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                #药不然    
                elif this_player[0]["role"] == 6:
                    player_list = []
                    role_list = []
                    for player in res_players:
                        if player["role"] != 6:
                            role_list.append(player["role"])
                            player_list.append(player["color"])
                    if intcmd == 0:
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r3_skill_obj = 0)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你未使用技能，游戏继续！\n"+Atq_Menu(db,intcmd,user,1)
                    elif (intcmd in player_list):
                        #改变其他人玩家表
                        atq_attack(db,intcmd,user,3)
                        #改变自己玩家表和房间表
                        db.update('players',  where="id = \'"+user+"\'", flag = 1, r3_skill_obj = intcmd)
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                        return u"你本回合偷袭了"+atq_color(intcmd)+u"玩家\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1)
                else:
                    db.update('players',  where="id = \'"+user+"\'", flag = 1)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                    return u"你是"+atq_role(this_player[0]["role"])+u"，未知技能"+help_text+u"\n"+Atq_Menu(db,intcmd,user,1)
            #--------------------------------------传位处理----------------------------------------       
            elif (this_player[0]["color"] == cur_player) and game_state==19 and (0<=intcmd<=8):
                player_list = []
                for player in res_players:
                    if not player["flag"]:
                        player_list.append(player["color"])
                if player_list:
                    if(intcmd in player_list):
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state - 2 ,cur_player = intcmd)
                        return u"你已经成功传给了"+atq_color(intcmd)+u"玩家\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return Atq_Menu(db,intcmd,user,1) 
                elif intcmd == 0:
                    db.update('players',  where="room = "+str(room_id)+"", flag = 0)
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"你已经成功继续游戏\n"+Atq_Menu(db,intcmd,user,1)
                else:
                    return Atq_Menu(db,intcmd,user,1) 
            else:
                return Atq_Menu(db,intcmd,user,1)
        #第3轮等待发言    
        elif game_state == 20:
            if flag:
                if host_id == user:
                    return u"发言阶段，请等待发言阶段结束\n 继续游戏：0"+help_text
                else:
                    return u"进入发言阶段，发言阶段结束后，房主输入0继续游戏"+help_text
            elif host_id == user and intcmd == 0:
                #更新房间状态
                db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
            else:
                return Atq_Menu(db,intcmd,user,1)
        #第3轮录入鉴宝结果    
        elif 21 <= game_state <= 23 :
            atq = [
                    [ res_room[0]["a9_rd"],res_room[0]["a9_tf"]],
                    [ res_room[0]["a10_rd"],res_room[0]["a10_tf"]],
                    [ res_room[0]["a11_rd"],res_room[0]["a11_tf"]],
                    [ res_room[0]["a12_rd"],res_room[0]["a12_tf"]],
                  ]
            vp_atq = res_room[0]["vp_atq"]          
            voted_atq = [res_room[0]["r3_a1"],res_room[0]["r3_a2"]]
            if flag:
                if user != host_id:
                    return u"房主正在录入鉴宝结果，请等待他完成操作！\n"+help_text
                elif game_state == 21:
                    return u"请按下列提示选择票数最高的宝物：\n "+atq_atq(atq[0][0])+u"：1\n "+atq_atq(atq[1][0])+u"：2\n "+atq_atq(atq[2][0])+u"：3\n "+atq_atq(atq[3][0])+u"：4"+help_text
                elif game_state == 22:
                    #过滤已鉴定宝物信息
                    for num in range(4):
                        if atq[num][0] == voted_atq[0]:
                            del atq[num]
                            break
                    return u"本轮票数最高的宝物为："+atq_atq(voted_atq[0])+u"\n请按下列提示选择票数第2高的宝物：\n "+atq_atq(atq[0][0])+u"：1\n "+atq_atq(atq[1][0])+u"：2\n "+atq_atq(atq[2][0])+u"：3\n "+help_text
                elif game_state == 23:
                    return u"本轮票数最高的宝物为："+atq_atq(voted_atq[0])+u"\n本轮票数第2高的宝物为："+atq_atq(voted_atq[1])+u"\n 继续游戏：0\n 重新选择：1"+help_text
                else:
                    return u"房间状态号越界"
            else:
                if user != host_id:
                    return Atq_Menu(db,intcmd,user,1) 
                elif game_state == 21 and 1<= intcmd <= 4:
                    voted_atq[0] = atq[intcmd-1][0]
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,r3_a1 = voted_atq[0], r3_a2 = voted_atq[1])
                    return u"选择"+atq_atq(voted_atq[0])+u"成功！\n "+Atq_Menu(db,intcmd,user,1) 
                elif game_state == 22 and 1<= intcmd <= 3:
                    for num in range(4):
                        if atq[num][0] == voted_atq[0]:
                            del atq[num]
                            break
                    voted_atq[1] = atq[intcmd-1][0]
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,r3_a1 = voted_atq[0], r3_a2 = voted_atq[1])
                    return u"选择"+atq_atq(voted_atq[1])+u"成功！\n "+Atq_Menu(db,intcmd,user,1)
                elif game_state == 23 and 0<= intcmd <= 1:
                    if intcmd == 1:
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state - 2 ,r3_a1 = 0, r3_a2 = 0)
                        return u"取消成功！请重新选择宝物\n"+Atq_Menu(db,intcmd,user,1)
                    elif intcmd ==0:
                        voted_tf = 0
                        for num in range(4):
                            if atq[num][0] == voted_atq[0]:
                                if atq[num][1] == 1:
                                    vp_atq += 1
                            if atq[num][0] == voted_atq[1]:
                                voted_tf  = atq[num][1]
                                if atq[num][1] == 1:
                                    vp_atq += 1
                        db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 ,vp_atq = vp_atq)
                        return u"本轮票数最高的宝物为"+atq_atq(voted_atq[0])+u"：不公布真赝\n本轮票数第2高的宝物为"+atq_atq(voted_atq[1])+u"："+atq_tf(voted_tf)+u"\n\n"+Atq_Menu(db,intcmd,user,1)
                    else:
                        return u"选择越界"
                else:
                    return Atq_Menu(db,intcmd,user,1)
        #---------第3轮结束----------------------------------------------------------------------------------------------------------------
        
        #判断游戏是否结束
        elif game_state == 24:
            if flag:
                return u"请房主输入0继续游戏\n 继续游戏：0【房主操作】"+help_text
            elif host_id == user and intcmd == 0:
                num = res_room[0]["num"]
                vp_atq = res_room[0]["vp_atq"]
                if vp_atq >= atq_winvp(num) or vp_atq+4 < atq_winvp(num):
                    #跳入处理终局结算
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 2 )
                    return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
                else:
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1 )
                    return u"继续游戏成功！\n"+Atq_Menu(db,intcmd,user,1)
            else:
                return Atq_Menu(db,intcmd,user,1)
        #录入鉴人目标    
        elif game_state == 25 :
            pro_text=u""
            player_list = []
            for player in res_players:
                if player["color"] != this_player[0]["color"]:
                    player_list.append(player["color"])
                    pro_text = pro_text + u"\n "+atq_color(player["color"]) + u"玩家："+str(player["color"])
            if flag:
                if not this_player[0]["player_obj"]:
                    if 1<= this_player[0]["role"] <= 4 or this_player[0]["role"] == 8:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按要求选择老朝奉，所有玩家输入完成后，房主输入0继续游戏" + pro_text + help_text
                    elif this_player[0]["role"] == 5:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按要求选择许愿，所有玩家输入完成后，房主输入0继续游戏" + pro_text + help_text
                    elif this_player[0]["role"] == 6:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按要求选择方震，所有玩家输入完成后，房主输入0继续游戏" + pro_text + help_text
                    elif this_player[0]["role"] == 7:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，请按要求任选1名角色，所有玩家输入完成后，房主输入0继续游戏" + pro_text + help_text
                    else:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，未知鉴人目标"+help_text
                elif host_id == user:
                    if 1<= this_player[0]["role"] <= 4 or this_player[0]["role"] == 8:
                        return u"你是"+atq_role(this_player[0]["role"])+u"你已选择："+atq_color(this_player[0]["player_obj"])+u"玩家为老朝奉，可以输入对应编号更改目标\n请等待所有玩家完成选择\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 5:
                        return u"你是"+atq_role(this_player[0]["role"])+u"你已选择："+atq_color(this_player[0]["player_obj"])+u"玩家为许愿，可以输入对应编号更改目标\n请等待所有玩家完成选择\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 6:
                        return u"你是"+atq_role(this_player[0]["role"])+u"你已选择："+atq_color(this_player[0]["player_obj"])+u"玩家为方震，可以输入对应编号更改目标\n请等待所有玩家完成选择\n 继续游戏：0"+help_text
                    elif this_player[0]["role"] == 7:
                        return u"你是"+atq_role(this_player[0]["role"])+u"你已选择："+atq_color(this_player[0]["player_obj"])+u"玩家，请等待所有玩家完成选择\n 继续游戏：0"+help_text
                    else:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，未知鉴人目标"+help_text        
                else:
                    if 1<= this_player[0]["role"] <= 4 or this_player[0]["role"] == 8:
                        return u"你是"+atq_role(this_player[0]["role"])+u"你已选择："+atq_color(this_player[0]["player_obj"])+u"玩家为老朝奉，可以输入对应编号更改目标\n所有玩家输入完成后，房主输入0继续游戏" +help_text
                    elif this_player[0]["role"] == 5:
                        return u"你是"+atq_role(this_player[0]["role"])+u"你已选择："+atq_color(this_player[0]["player_obj"])+u"玩家为许愿，可以输入对应编号更改目标\n所有玩家输入完成后，房主输入0继续游戏"+help_text
                    elif this_player[0]["role"] == 6:
                        return u"你是"+atq_role(this_player[0]["role"])+u"你已选择："+atq_color(this_player[0]["player_obj"])+u"玩家为方震，可以输入对应编号更改目标\n所有玩家输入完成后，房主输入0继续游戏"+help_text
                    elif this_player[0]["role"] == 7:
                        return u"你是"+atq_role(this_player[0]["role"])+u"你已选择："+atq_color(this_player[0]["player_obj"])+u"玩家\n所有玩家输入完成后，房主输入0继续游戏"+help_text
                    else:
                        return u"你是"+atq_role(this_player[0]["role"])+u"，未知鉴人目标"+help_text
            elif (intcmd in player_list):
                db.update('players',  where="id = \'"+user+"\'", player_obj = intcmd )
                return u"选择"+atq_color(intcmd)+u"成功！\n"+Atq_Menu(db,intcmd,user,1)
            elif host_id == user and intcmd == 0: 
                check_obj = 0
                for player in res_players:
                    if player["player_obj"] == 0:
                        check_obj = 1 
                if check_obj:
                    return u"有玩家尚未选择请耐心等待！\n"+Atq_Menu(db,intcmd,user,1)
                else:
                    db.update('rooms', where="id = "+str(room_id)+"", state = game_state + 1)
                    return u"鉴人目标选择完成！\n"+Atq_Menu(db,intcmd,user,1)
            else:
                return Atq_Menu(db,intcmd,user,1)
        #输出终局信息        
        elif game_state == 26 :
            return atq_over(db,user) + help_text    
        else:    
            return u"游戏进程越界！"
            

def room_create(db,intcmd,user):
    '创建房间函数'
    if intcmd > 8 or intcmd < 6:
        return u"游戏人数超出范围\n"+Atq_Menu(db,intcmd,user,1)
    #生成随机6位房间号
    room_id = int(random.randrange(100000,999999,1))
    while list(db.select('rooms' , where="id = \'"+str(room_id)+"\'")):
         room_id = int(random.randrange(100000,999999,1))
    #随机分配宝物
    atq_round = [1,2,3,4,5,6,7,8,9,10,11,12]
    atq_tf1 = [1,1,0,0]
    atq_tf2 = [1,1,0,0]
    atq_tf3 = [1,1,0,0]
    random.shuffle(atq_round)
    random.shuffle(atq_tf1)
    random.shuffle(atq_tf2)
    random.shuffle(atq_tf3)
    #创建房间表
    db.insert('rooms', id=room_id, host=user, num=intcmd, state=0, cur_player=0, vp_atq=0, vp_player=0, vp_total=0, 
              a1_rd=atq_round[0], a1_tf=atq_tf1[0], a2_rd=atq_round[1], a2_tf=atq_tf1[1], a3_rd=atq_round[2], a3_tf=atq_tf1[2], a4_rd=atq_round[3], a4_tf=atq_tf1[3], 
              a5_rd=atq_round[4], a5_tf=atq_tf2[0], a6_rd=atq_round[5], a6_tf=atq_tf2[1], a7_rd=atq_round[6], a7_tf=atq_tf2[2], a8_rd=atq_round[7], a8_tf=atq_tf2[3],
              a9_rd=atq_round[8], a9_tf=atq_tf3[0], a10_rd=atq_round[9], a10_tf=atq_tf3[1], a11_rd=atq_round[10], a11_tf=atq_tf3[2], a12_rd=atq_round[11], a12_tf=atq_tf3[3],
              a1_state=0,a2_state=0,a3_state=0,a4_state=0,a5_state=0,a6_state=0,a7_state=0,a8_state=0,a9_state=0,a10_state=0,a11_state=0,a12_state=0,
              r1_a1=0,r1_a2=0,r2_a1=0,r2_a2=0,r3_a1=0,r3_a2=0
             )
    #创建玩家表
    db.insert('players', id = user, room = room_id, flag = 0, color = 0, role = 0, mate = 0, r1_state = 0, r2_state = 0, r3_state = 0,r1_skill_obj=99, r2_skill_obj=99, r3_skill_obj=99, player_obj = 0 )
    return u"创建"+str(intcmd)+u"人房间成功！"+Atq_Menu(db,intcmd,user,1)

def room_join(db,intcmd,user):
    '加入房间函数'
    results = list(db.select('rooms' , where="id = "+str(intcmd)+""))
    if not results:
        return u"你输入的房间号不存在，加入房间失败\n"+Atq_Menu(db,intcmd,user,1)
    else:
        room_id = results[0]["id"]
        num_room = results[0]["num"]
        num_players = len(list(db.select('players' , where="room = "+str(room_id)+"")))
        if num_players >= num_room:
            return u"房间"+str(room_id)+u"人数已满，请重新输入！\n"+Atq_Menu(db,intcmd,user,1)
        else:
            #创建玩家表
            db.insert('players', id = user, room = room_id, flag = 0, color = 0, role = 0, mate = 0, r1_state = 0, r2_state = 0, r3_state = 0, r1_skill_obj=99, r2_skill_obj=99, r3_skill_obj=99, player_obj = 0)
            return u"加入"+str(num_room)+u"人房间成功！\n"+Atq_Menu(db,intcmd,user,1)

def atq_attack(db,intcmd,user,cur_round):
    '药不然偷袭函数，在数据库完成状态更新'
    this_player = list(db.select('players' , where="id = \'"+user+"\'"))
    room_id = this_player[0]["room"]
    res_players = list(db.select('players' , where="room = "+str(room_id)+""))
    xy_id = fz_id = jyf_id = ""
    for player in res_players:
        if player["color"] == intcmd:
            cur_id = player["id"]
            cur_flag = player["flag"]
            cur_state = [ player["r1_state"],player["r2_state"],player["r3_state"]]
        if player["role"] == 1:
            xy_id = player["id"]
            xy_flag = player["flag"]
            xy_state = [ player["r1_state"],player["r2_state"],player["r3_state"]]
        elif player["role"] == 2:
            fz_id = player["id"]
        elif player["role"] == 8:
            jyf_id = player["id"]    
    #处理方震        
    if cur_id == fz_id:
        #处理方震
        #本轮未行动
        if cur_flag == 0 :
            #本轮未被偷袭：+0
            if cur_state[cur_round-1] != 1:
                cur_state[cur_round-1] = 1
            #本轮已被偷袭：+1
            elif cur_round <=2 and cur_state[cur_round-1] == 1:
                cur_state[cur_round] = 1
        #本轮已行动
        elif cur_flag == 1:
            if cur_round <= 2:
                #下轮未被偷袭：+1
                if cur_state[cur_round] != 1:
                    cur_state[cur_round] = 1
                #下轮已被偷袭：+2
                elif cur_round <=1 and cur_state[cur_round] == 1:
                    cur_state[cur_round + 1] = 1
        db.update('players',  where="id = \'"+cur_id+"\'",r1_state = cur_state[0], r2_state = cur_state[1], r3_state = cur_state[2]  ) 
        #处理许愿
        #本轮未行动
        if xy_flag == 0 :
            #本轮未被偷袭：+0
            if xy_state[cur_round-1] != 1:
                xy_state[cur_round-1] = 1
            #本轮已被偷袭：+1
            elif cur_round <=2 and xy_state[cur_round-1] == 1:
                xy_state[cur_round] = 1
        #本轮已行动
        elif xy_flag == 1:
            if xy_round <= 2:
                #下轮未被偷袭：+1
                if xy_state[cur_round] != 1:
                    xy_state[cur_round] = 1
                #下轮已被偷袭：+2
                elif cur_round <=1 and xy_state[cur_round] == 1:
                    xy_state[cur_round + 1] = 1
        db.update('players',  where="id = \'"+xy_id+"\'",r1_state = xy_state[0], r2_state = xy_state[1], r3_state = xy_state[2]  ) 
    elif cur_id == jyf_id:
        jyf_state = [2,2,2]
        #本轮未行动
        if cur_flag == 0 :
            #本轮未被偷袭：+0
            if cur_state[cur_round-1] != 1:
                jyf_state[cur_round-1] = 1
            #本轮已被偷袭：+1
            elif cur_round <=2 and cur_state[cur_round-1] == 1:
                jyf_state[cur_round] = 1
        #本轮已行动
        elif cur_flag == 1:
            if cur_round <= 2:
                #下轮未被偷袭：+1
                if cur_state[cur_round] != 1:
                    jyf_state[cur_round] = 1
                #下轮已被偷袭：+2
                elif cur_round <=1 and cur_state[cur_round] == 1:
                    jyf_state[cur_round + 1] = 1
        db.update('players',  where="id = \'"+cur_id+"\'",r1_state = jyf_state[0], r2_state = jyf_state[1], r3_state = jyf_state[2]  ) 
    else:
        #本轮未行动
        if cur_flag == 0 :
            #本轮未被偷袭：+0
            if cur_state[cur_round-1] != 1:
                cur_state[cur_round-1] = 1
            #本轮已被偷袭：+1
            elif cur_round <=2 and cur_state[cur_round-1] == 1:
                cur_state[cur_round] = 1
        #本轮已行动
        elif cur_flag == 1:
            if cur_round <= 2:
                #下轮未被偷袭：+1
                if cur_state[cur_round] != 1:
                    cur_state[cur_round] = 1
                #下轮已被偷袭：+2
                elif cur_round <=1 and cur_state[cur_round] == 1:
                    cur_state[cur_round + 1] = 1
        db.update('players',  where="id = \'"+cur_id+"\'",r1_state = cur_state[0], r2_state = cur_state[1], r3_state = cur_state[2]  )             

def atq_over(db,user):
    '结果打印函数，输出游戏最终结果'
    this_player = list(db.select('players' , where="id = \'"+user+"\'"))
    room_id = this_player[0]["room"]
    res_room = list(db.select('rooms' , where="id = "+str(room_id)+""))
    res_players = list(db.select('players' , where="room = "+str(room_id)+""))
    num_room = res_room[0]["num"]
    vp_atq = res_room[0]["vp_atq"]
    vp_player = 0
    vp_total = 0 
    atq = [
           [ res_room[0]["a1_rd"],res_room[0]["a1_tf"]],
           [ res_room[0]["a2_rd"],res_room[0]["a2_tf"]],
           [ res_room[0]["a3_rd"],res_room[0]["a3_tf"]],
           [ res_room[0]["a4_rd"],res_room[0]["a4_tf"]],
           [ res_room[0]["a5_rd"],res_room[0]["a5_tf"]],
           [ res_room[0]["a6_rd"],res_room[0]["a6_tf"]],
           [ res_room[0]["a7_rd"],res_room[0]["a7_tf"]],
           [ res_room[0]["a8_rd"],res_room[0]["a8_tf"]],
           [ res_room[0]["a9_rd"],res_room[0]["a9_tf"]],
           [ res_room[0]["a10_rd"],res_room[0]["a10_tf"]],
           [ res_room[0]["a11_rd"],res_room[0]["a11_tf"]],
           [ res_room[0]["a12_rd"],res_room[0]["a12_tf"]]
          ]
    #打印鉴宝回合结果
    pro_text = u"游戏结束，观看后请点击菜单退出游戏\n"
    count = 1 
    for antique in atq:
        pro_text = pro_text + atq_atq(antique[0])+u"（"+atq_tf(antique[1])+u" ）"
        if count%4 == 0:
            pro_text = pro_text + u"\n"
        else:    
            pro_text = pro_text + u"，"
        count += 1 
    pro_text = pro_text + u"许愿阵营鉴宝回合得分："+str(vp_atq)+u"\n"    
    #游戏是否提前结束
    if vp_atq >= atq_winvp(num_room) or vp_atq+4 < atq_winvp(num_room):
        if vp_atq >= atq_winvp(num_room):
            res_text = u"许愿阵营获胜！\n"
        else:
            res_text = u"老朝奉阵营获胜！\n"
        return pro_text
    #打印鉴人回合结果
    xy_color = fz_color = lcf_color = ybr_color = lcf_obj = ybr_obj = 0
    for player in res_players:
        if player["role"] == 1:
            xy_color = player["color"] 
        elif player["role"] == 2:
            fz_color = player["color"]
        elif player["role"] == 5:
            lcf_color = player["color"]
            lcf_obj = player["player_obj"]
        elif player["role"] == 6:
            ybr_color = player["color"]
            ybr_obj = player["player_obj"]
    num_good = 0
    num_right = 0
    pro_text = pro_text + u"\n选择老朝奉：\n" 
    for player in res_players:
        if 1 <= player["role"] <=4 or player["role"] ==8:
            pro_text = pro_text + atq_color(player["color"])+u"玩家选择："+ atq_color(player["player_obj"])+u"玩家\n"
            num_good += 1
            if player["player_obj"] == lcf_color:
                num_right += 1
    if num_right > float(num_good) / 2.0:
        res_text = u"成功找出\n"
        vp_player += 1
    else:
        res_text = u"未被找出\n"
    pro_text = pro_text + atq_color(lcf_color)+u"玩家是真正的老朝奉："+ res_text             
    pro_text = pro_text + u"\n选择许愿：\n"
    pro_text = pro_text + atq_color(lcf_color)+u"玩家选择："+ atq_color(lcf_obj)+u"玩家\n"
    if lcf_obj == xy_color:
        res_text = u"成功找出\n"
    else:
        res_text = u"未被找出\n"
        vp_player += 2
    pro_text = pro_text + atq_color(xy_color)+u"玩家是真正的许愿："+ res_text
    pro_text = pro_text + u"\n选择方震：\n"
    pro_text = pro_text + atq_color(ybr_color)+u"玩家选择："+ atq_color(ybr_obj)+u"玩家\n"
    if ybr_obj == fz_color:
        res_text = u"成功找出\n"
    else:
        res_text = u"未被找出\n"
        vp_player += 1
    pro_text = pro_text + atq_color(fz_color)+u"玩家是真正的方震："+ res_text  
    pro_text = pro_text + u"许愿阵营鉴人回合得分："+str(vp_player)+u"\n\n"
    vp_total = vp_atq + vp_player
    if vp_total >= atq_winvp(num_room):
        res_text = u"许愿阵营获胜！\n"
    else:
        res_text = u"老朝奉阵营获胜！\n"
    pro_text = pro_text + u"许愿阵营总得分："+str(vp_total)+u"\n" + res_text    
    db.update('rooms', where="id = "+str(room_id)+"", vp_player = vp_player, vp_total = vp_total)    
    return pro_text
            
def atq_color(color):
    '颜色号转换成颜色字符'
    if color == 1:
        return u"红色"
    elif color == 2:
        return u"橙色"
    elif color == 3:
        return u"黄色"
    elif color == 4:
        return u"蓝色"
    elif color == 5:
        return u"绿色"
    elif color == 6:
        return u"紫色"
    elif color == 7:
        return u"黑色"
    elif color == 8:
        return u"白色"
    else:
        return u"未知颜色"
    
def atq_role(role):
    '角色号转换成角色字符'
    if role == 1:
        return u"许愿"
    elif role == 2:
        return u"方震"
    elif role == 3:
        return u"黄烟烟"
    elif role == 4:
        return u"木户加奈"
    elif role == 5:
        return u"老朝奉"
    elif role == 6:
        return u"药不然"
    elif role == 7:
        return u"郑国渠"
    elif role == 8:
        return u"姬云浮"
    else:
        return u"未知角色"
    
def atq_atq(atq):
    '古董号转换成兽首字符'
    if atq == 1:
        return u"鼠首"
    elif atq == 2:
        return u"牛首"
    elif atq == 3:
        return u"虎首"
    elif atq == 4:
        return u"兔首"
    elif atq == 5:
        return u"龙首"
    elif atq == 6:
        return u"蛇首"
    elif atq == 7:
        return u"马首"
    elif atq == 8:
        return u"羊首"
    elif atq == 9:
        return u"猴首"
    elif atq == 10:
        return u"鸡首"
    elif atq == 11:
        return u"狗首"
    elif atq == 12:
        return u"猪首"
    else:
        return u"未知兽首"

def atq_tf(flag):
    '真假结果转化为字符'
    if flag == 0:
        return u"赝品"
    elif flag == 1:
        return u"真品"
    elif flag == 2:
        return u"被偷袭"
    elif flag == 3:
        return u"无法鉴定"                                                              
    else:
        return u"未知结果"    
    
def atq_ptf(flag):
    '阵营结果转化为字符'
    if flag == 0:
        return u"老朝奉阵营"
    elif flag == 1:
        return u"许愿阵营"                                                             
    else:
        return u"未知阵营" 
    
def atq_winvp(num):
    '不同游戏人数下许愿阵营获胜获胜分数'
    error = 0
    if num == 6:
        return 6
    elif num == 7:
        return 6
    elif num == 8:
        return 6
    else:
        return error