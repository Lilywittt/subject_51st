# 左上角显示剧情中日期
screen date(year, month, day):
    $ date_to_display = year + "年" + month + "月" + day + "日"
    text date_to_display xalign 0.0 yalign 0.0 size 25


# 右上角显示当前Chapter名
screen chapter(chapter_content):
    text chapter_content xalign 1.0 yalign 0.0 size 25


# 转场时显示当前Episode名
screen episode(episode_content):
    text episode_content:
        xalign 0.5 yalign 0.5 size 50
        at transform:
            alpha 0.0
            linear 1.0 alpha 1.0
            time 2.0
            linear 1.0 alpha 0.0


image bg test_bg = "bg/homura.png"