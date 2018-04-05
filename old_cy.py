import urllib, urllib2, time


#2015년 9월 30일 url
url = 'http://minihp.cyworld.com/pims/board/general/board_view.asp?domain=&tid=51979806&board_no=26&search_type=&search_keyword=&item_seq=23589247&cpage=1&list_type=2'
test = False
while test == False:
    cookie = '''LOGIN=logincid=&savecid=; cookieinfouser=56e0b2c768666ac644cd6a505775cd6b45a1647d5d1fe1303ce4fdb889d4316ac56378a67f8e32718a99906d78b24aa368ca6ac574322e110f73cbc566a26ce46b3fd110cafd8e737589037532d75e7e122ac5560be421ae096d62cfc83e0be56276bb1612406ce9a867d1f06123ab0540f98909295289abc59088f97c79a672ae674d666da24b554ec0a1c95fe9c55ef860e2eefb1ec4adfce5b77a16f5b71e; MAIN=BIRTHDAY=19920510&FILE_Referer=True&OpenSession=1&mem_ivtCnfm=1&rkey=51979806705547511577&logincount=5343&onedegrees_cnt=0&REPL=&GIFT=&arrActiveEffect=; NSVC=NickID=51979806|%B1%E8%B5%BF%C7%F6|1|&MainBlog=&MainBlogNick=&MainHomeName=%B1%E8%B5%BF%C7%F6&MainHome=M&miniHomeType=0&MoaUse=T&Login=1; CFN=8fdf65fe9c5058bbf3e2e8b8c79b295dddf72d08da003de005705ae93a8c20e41a214e9d3dea2c803022c5bd3e2236614244b186243e33583d9ea6681dc372238a534f7bd05f5e999cd5353841ace368899080deec63de808f4e0e5ad52f74cd0f6806ac00ae827876a408dd20af5684897319230d49be4000f1dbaa5f87db2056a7516d617df8cb74d7e074fbb241f40d1f23715977693782fc448aae83babca21464503b5c00f07629070f7016736bd2ce282fc3acfde1a2ae7d34d5f638bd8f52efdb102fa83f732b4e45238763659613041de4234103b5361e7020c391c4c696dd08a8e92cccda057f1b1f637511c6fab84e9717b7711f93acf7ef6a0119; C3RD=435e33cbbcf515462f7483757059b33f41ffc9db891e38c8f0986a3b630177f17d2698bf3e4c40cb8ec42a642184e00d22bc56917ba23133b220b631a313af1e40b0ca62c725ee92c8e45b72c33be058c8c702300d3efba4a0880f76a38530f66bd5f24cf2f63fdbcd5d7942dd5a981c170843bfaf287e7ebd7bc096b6f9b0aadff6fd9eb24af072c5ab49436f77b56c; ETC=enc%5Fnateon%5Femail=&cpinfo=03d6f49b3acf1338cabc8d79b2badccfc0cad6a83a0107868e9e1dcd50bce9ea97833846693bffa5f27a2176759be17afeb716d795af89e21f802c49a0a733da&NCFLAG=n&CFN=8fdf65fe9c5058bbf3e2e8b8c79b295d940da64b0c8fcd873327e6bdc9d3280bd289d3e72b7f27085d05c43dd652db574234c458f722e3bed4af03410d68633beb081e4bdfd2d411df50dbc77ccbb5ecd499a4f69024826aaeb49d4db28a8cb32b9590c085597a245371c37313b81e982a5462806367a0b0cd9d941affcfa791f1527e4f6389cb7cbd3114c5bcaed885d574894b67361752e7905b09055ea7d937fa386ec823d2592f6b72f2e7a4c3ca2c4839f4e604ffe24c9f974d8864f4c37e46d7357344a2ff9fc12e60490caa2ef887cf9f646918b4b0395cdf7a98a34d07b54954a80d2e43af379a9ef692933d1cea7aa5a5a816bdaa181b3570c12870; UD3=na90ea7320b709c3ce2fb5abe528038d; ndrn=|NTE5Nzk4MDY=|; UA3=|NTE5Nzk4MDY=|; RDB=01|22|||KR|; UAKD=3; NateMain=Loc=&Sync=0215; CyMain=moafocus=false; MINIHP=tid=51979806&minihp_tap=K&minihp_news=B&minihp_banner=0&minihp_banner_src=guide_n&dayVisitCnt=0&totVisitCnt=0&profile_bopen=1&profile_breply=1&diary_bopen=1&jukebox_bopen=1&img_bopen=1&sketch_bopen=0&bbs_bopen=1&visit_bopen=1&link_bopen=0&miniroom_bopen=1&miniroom_breply=0&diary_breply=1&jukebox_breply=1&img_breply=1&sketch_breply=1&bbs_breply=1&visit_breply=1&link_breply=0&storyroom_bopen=1&storyroom_breply=1&video_bopen=1&video_breply=1&photoreply_breply=0&minihp_title=%b1%ba%b4%eb%b0%a8&openClub=0&openSymbol=1&minihp_domain=I_love_red&minihp_searchOpen=0&h1n=&mainroom=0&surprise_tag_cnt=1&reputation_bopen=0&reputation_idx=&reputation_use=&MySymbol_seq=&pbuse=&onedegnote_bopen=1&C2id=&bbsWide=0&sktWide=1&home_setting=3%7c1%2c3%2c2%2c%2c%2c&newscrap=0&minilife_bopen=1&minilife_url=&nate_id=&gendercd=1&blunar=1&birthday=1992.5+.10&email=qkakwkskekdk%40hanmail.net&tName=%b1%e8%b5%bf%c7%f6&minihp_alert=&main_alert=&deg_group=d0f6bcb497a01f6e55235c234f27d507&nidByTid=&reply_up_tm=2011-12-06&onedegnotecommentyn=1&onedegnotecolor=++++++&pbox_bopen=0&imgWide=0&imgWideType=1&imgFolderViewLevel=1&imgAlign=2&IsAllowGlobalReply=1&simg_bopen=0&userId=51979806; pcid=142397751159370205; ROOM=SR_storyroom_seq=; MY=s=0'''
    request = urllib2.Request(url)
    request.add_header('cookie', cookie)
    response = urllib2.urlopen(request).read()
    s = '''%s''' % (response)
    next_link = s

    #제목 추출
    title_date = s.find('<dt>작성일</dt>')
    title_d = s[title_date+43:title_date+48]

    title_name_s = s.find('board-title">')
    title_name_e = s.find('<a href="javascript:ndrStatClick')
    title_n = s[title_name_s+17:title_name_e]
    title = title_d + title_n
    title = title.translate(None, '?,/,\,|,*,<,>,"')
    print(title + "\n")

    #게시글 본문 추출
    start = s.find('<!-- 글 내용 -->')
    end = s.find('<!-- 체크인 -->')
    s = s[start+17:end-1]

    #게시글 앞뒤 스크립트 제거
    start2 = s.find('</STYLE>')
    end2 = s.find('<!-- 본문보기')
    s = s[start2+8:end2]
    s = s.split('<div>')
    s = ''.join(s)
    s = s.split('</div>')
    s = ''.join(s)
    s = s.split('<br>')
    s = '\n'.join(s)
    s = s.split('<P>')
    s = ''.join(s)
    s = s.split('</P>')
    s = ''.join(s)
    s = s.split('&nbsp;')
    s = ''.join(s)
    print(s)

    #다음 링크 추출
    start = next_link.find('<!-- 이전글/다음글/관련글 목록  -->')
    end = next_link.find('현재 :</dt>')
    next_link = next_link[start:end+11]

    start2 = next_link.find('<dd>')
    end2 = next_link.find('</dd>')
    next_link = next_link[start2+16:end2-5]

    end3 = next_link.find('>')
    next_link = next_link[:end3-1]

    test = next_link == '없습니'

    #다음가야 할 url
    url = 'http://minihp.cyworld.com/pims/board/general/' + next_link
    
    

    f = file(title+'.txt', 'w')
    f.write(s)
    f.close()

    time.sleep(0.8)

raw_input('Press the Enter key.')
#for문 돌릴 방법만 찾으면 됨
