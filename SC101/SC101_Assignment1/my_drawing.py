"""
File: Stay at home, please.
Name: Elven
----------------------
This dog looks at you firmly. His eyes convey the message: 'Please stay home at home or you will get COVID-19!!!'
"""

from campy.graphics.gobjects import GOval, GRect, GPolygon
from campy.graphics.gwindow import GWindow

window = GWindow(width=500, height=706)

def main():
    """
    This part is background
    """
    back = GPolygon()
    back.add_vertex((0, 0))
    back.add_vertex((0, window.height))
    back.add_vertex((window.width, window.height))
    back.add_vertex((window.width, 0))
    back.filled = True
    back.fill_color = '#4f4d4e'
    back.color = '#4f4d4e'
    window.add(back)

    """
    This part is left ear
    """

    l_ear_1 = GPolygon()
    l_ear_1.add_vertex((172, 95))
    l_ear_1.add_vertex((191, 110))
    l_ear_1.add_vertex((183, 117))
    l_ear_1.add_vertex((161, 115))
    l_ear_1.add_vertex((157, 104))
    l_ear_1.filled = True
    l_ear_1.fill_color = '#36383e'
    l_ear_1.color = '#36383e'
    window.add(l_ear_1)

    l_ear_2 = GPolygon()
    l_ear_2.add_vertex((157, 104))
    l_ear_2.add_vertex((118, 184))
    l_ear_2.add_vertex((107, 221))
    l_ear_2.add_vertex((122, 186))
    l_ear_2.add_vertex((161, 115))
    l_ear_2.filled = True
    l_ear_2.fill_color = '#4f4d4e'
    l_ear_2.color = '#4f4d4e'
    window.add(l_ear_2)

    l_ear_3 = GPolygon()
    l_ear_3.add_vertex((161, 115))
    l_ear_3.add_vertex((122, 186))
    l_ear_3.add_vertex((143, 194))
    l_ear_3.add_vertex((161, 172))
    l_ear_3.filled = True
    l_ear_3.fill_color = '#9eaab2'
    l_ear_3.color = '#9eaab2'
    window.add(l_ear_3)

    l_ear_5 = GPolygon()
    l_ear_5.add_vertex((183, 117))
    l_ear_5.add_vertex((161, 115))
    l_ear_5.add_vertex((161, 172))
    l_ear_5.add_vertex((228, 217))
    l_ear_5.filled = True
    l_ear_5.fill_color = '#aeb6be'
    l_ear_5.color = '#aeb6be'
    window.add(l_ear_5)

    l_ear_6 = GPolygon()
    l_ear_6.add_vertex((183, 117))
    l_ear_6.add_vertex((191, 110))
    l_ear_6.add_vertex((228, 217))
    l_ear_6.filled = True
    l_ear_6.fill_color = '#232429'
    l_ear_6.color = '#232429'
    window.add(l_ear_6)

    l_ear_7 = GPolygon()
    l_ear_7.add_vertex((191, 110))
    l_ear_7.add_vertex((228, 217))
    l_ear_7.add_vertex((215, 155))
    l_ear_7.filled = True
    l_ear_7.fill_color = '#383e43'
    l_ear_7.color = '#383e43'
    window.add(l_ear_7)

    l_ear_8 = GPolygon()
    l_ear_8.add_vertex((107, 221))
    l_ear_8.add_vertex((96, 291))
    l_ear_8.add_vertex((141, 301))
    l_ear_8.filled = True
    l_ear_8.fill_color = '#c8c7c7'
    l_ear_8.color = '#c8c7c7'
    window.add(l_ear_8)

    l_ear_9 = GPolygon()
    l_ear_9.add_vertex((107, 221))
    l_ear_9.add_vertex((141, 301))
    l_ear_9.add_vertex((175, 266))
    l_ear_9.filled = True
    l_ear_9.fill_color = '#9e9d9d'
    l_ear_9.color = '#9e9d9d'
    window.add(l_ear_9)

    l_ear_10 = GPolygon()
    l_ear_10.add_vertex((122, 186))
    l_ear_10.add_vertex((107, 221))
    l_ear_10.add_vertex((175, 266))
    l_ear_10.add_vertex((143, 194))
    l_ear_10.filled = True
    l_ear_10.fill_color = '#9b9794'
    l_ear_10.color = '#9b9794'
    window.add(l_ear_10)

    l_ear_11 = GPolygon()
    l_ear_11.add_vertex((161, 172))
    l_ear_11.add_vertex((143, 194))
    l_ear_11.add_vertex((175, 266))
    l_ear_11.add_vertex((182, 240))
    l_ear_11.filled = True
    l_ear_11.fill_color = '#5c514c'
    l_ear_11.color = '#5c514c'
    window.add(l_ear_11)

    l_ear_12 = GPolygon()
    l_ear_12.add_vertex((161, 172))
    l_ear_12.add_vertex((182, 240))
    l_ear_12.add_vertex((228, 217))
    l_ear_12.filled = True
    l_ear_12.fill_color = '#c3c2c5'
    l_ear_12.color = '#c3c2c5'
    window.add(l_ear_12)

    """
    This part is right ear.
    """
    r_ear_1 = GPolygon()
    r_ear_1.add_vertex((346, 90))
    r_ear_1.add_vertex((332, 105))
    r_ear_1.add_vertex((336, 117))
    r_ear_1.add_vertex((357, 113))
    r_ear_1.add_vertex((361, 100))
    r_ear_1.filled = True
    r_ear_1.fill_color = '#3f4247'
    r_ear_1.color = '#3f4247'
    window.add(r_ear_1)

    r_ear_2 = GPolygon()
    r_ear_2.add_vertex((332, 105))
    r_ear_2.add_vertex((313, 132))
    r_ear_2.add_vertex((316, 138))
    r_ear_2.add_vertex((336, 117))
    r_ear_2.filled = True
    r_ear_2.fill_color = '#5a616a'
    r_ear_2.color = '#5a616a'
    window.add(r_ear_2)

    r_ear_2 = GPolygon()
    r_ear_2.add_vertex((332, 105))
    r_ear_2.add_vertex((313, 132))
    r_ear_2.add_vertex((316, 138))
    r_ear_2.add_vertex((336, 117))
    r_ear_2.filled = True
    r_ear_2.fill_color = '#5a616a'
    r_ear_2.color = '#5a616a'
    window.add(r_ear_2)

    r_ear_3 = GPolygon()
    r_ear_3.add_vertex((313, 132))
    r_ear_3.add_vertex((316, 138))
    r_ear_3.add_vertex((288, 217))
    r_ear_3.filled = True
    r_ear_3.fill_color = '#383d42'
    r_ear_3.color = '#383d42'
    window.add(r_ear_3)

    r_ear_4 = GPolygon()
    r_ear_4.add_vertex((336, 117))
    r_ear_4.add_vertex((316, 138))
    r_ear_4.add_vertex((288, 217))
    r_ear_4.add_vertex((332, 178))
    r_ear_4.filled = True
    r_ear_4.fill_color = '#a7b7c0'
    r_ear_4.color = '#a7b7c0'
    window.add(r_ear_4)

    r_ear_5 = GPolygon()
    r_ear_5.add_vertex((336, 117))
    r_ear_5.add_vertex((332, 178))
    r_ear_5.add_vertex((353, 193))
    r_ear_5.add_vertex((373, 177))
    r_ear_5.add_vertex((357, 113))
    r_ear_5.filled = True
    r_ear_5.fill_color = '#b0b8c4'
    r_ear_5.color = '#b0b8c4'
    window.add(r_ear_5)

    r_ear_6 = GPolygon()
    r_ear_6.add_vertex((357, 113))
    r_ear_6.add_vertex((373, 177))
    r_ear_6.add_vertex((396, 171))
    r_ear_6.filled = True
    r_ear_6.fill_color = '#929ea8'
    r_ear_6.color = '#929ea8'
    window.add(r_ear_6)

    r_ear_7 = GPolygon()
    r_ear_7.add_vertex((357, 113))
    r_ear_7.add_vertex((361, 100))
    r_ear_7.add_vertex((396, 171))
    r_ear_7.filled = True
    r_ear_7.fill_color = '#35343a'
    r_ear_7.color = '#35343a'
    window.add(r_ear_7)

    r_ear_8 = GPolygon()
    r_ear_8.add_vertex((332, 178))
    r_ear_8.add_vertex((288, 217))
    r_ear_8.add_vertex((338, 237))
    r_ear_8.filled = True
    r_ear_8.fill_color = '#c4c8ce'
    r_ear_8.color = '#c4c8ce'
    window.add(r_ear_8)

    r_ear_9 = GPolygon()
    r_ear_9.add_vertex((332, 178))
    r_ear_9.add_vertex((353, 193))
    r_ear_9.add_vertex((338, 237))
    r_ear_9.filled = True
    r_ear_9.fill_color = '#b0b4ba'
    r_ear_9.color = '#b0b4ba'
    window.add(r_ear_9)

    r_ear_10 = GPolygon()
    r_ear_10.add_vertex((373, 177))
    r_ear_10.add_vertex((353, 193))
    r_ear_10.add_vertex((338, 237))
    r_ear_10.add_vertex((372, 235))
    r_ear_10.filled = True
    r_ear_10.fill_color = '#62544f'
    r_ear_10.color = '#62544f'
    window.add(r_ear_10)

    r_ear_11 = GPolygon()
    r_ear_11.add_vertex((373, 177))
    r_ear_11.add_vertex((372, 235))
    r_ear_11.add_vertex((397, 203))
    r_ear_11.add_vertex((396, 171))
    r_ear_11.filled = True
    r_ear_11.fill_color = '#a1a7af'
    r_ear_11.color = '#a1a7af'
    window.add(r_ear_11)

    r_ear_12 = GPolygon()
    r_ear_12.add_vertex((396, 171))
    r_ear_12.add_vertex((397, 203))
    r_ear_12.add_vertex((418, 236))
    r_ear_12.filled = True
    r_ear_12.fill_color = '#3c4244'
    r_ear_12.color = '#3c4244'
    window.add(r_ear_12)

    r_ear_13 = GPolygon()
    r_ear_13.add_vertex((338, 237))
    r_ear_13.add_vertex((344, 263))
    r_ear_13.add_vertex((372, 235))
    r_ear_13.filled = True
    r_ear_13.fill_color = '#7d8b94'
    r_ear_13.color = '#7d8b94'
    window.add(r_ear_13)

    r_ear_13 = GPolygon()
    r_ear_13.add_vertex((338, 237))
    r_ear_13.add_vertex((344, 263))
    r_ear_13.add_vertex((372, 235))
    r_ear_13.filled = True
    r_ear_13.fill_color = '#7d8b94'
    r_ear_13.color = '#7d8b94'
    window.add(r_ear_13)

    r_ear_14 = GPolygon()
    r_ear_14.add_vertex((372, 235))
    r_ear_14.add_vertex((344, 263))
    r_ear_14.add_vertex((380, 288))
    r_ear_14.filled = True
    r_ear_14.fill_color = '#564c4b'
    r_ear_14.color = '#564c4b'
    window.add(r_ear_14)

    r_ear_14 = GPolygon()
    r_ear_14.add_vertex((397, 203))
    r_ear_14.add_vertex((372, 235))
    r_ear_14.add_vertex((380, 288))
    r_ear_14.add_vertex((424, 300))
    r_ear_14.add_vertex((418, 236))
    r_ear_14.filled = True
    r_ear_14.fill_color = '#a8adae'
    r_ear_14.color = '#a8adae'
    window.add(r_ear_14)

    """
    This part is upper head
    """
    u_head_1 = GPolygon()
    u_head_1.add_vertex((96, 291))
    u_head_1.add_vertex((93, 323))
    u_head_1.add_vertex((141, 301))
    u_head_1.filled = True
    u_head_1.fill_color = '#2d2c2d'
    u_head_1.color = '#2d2c2d'
    window.add(u_head_1)

    u_head_2 = GPolygon()
    u_head_2.add_vertex((93, 323))
    u_head_2.add_vertex((95, 372))
    u_head_2.add_vertex((118, 385))
    u_head_2.add_vertex((150, 363))
    u_head_2.add_vertex((141, 301))
    u_head_2.filled = True
    u_head_2.fill_color = '#2d3036'
    u_head_2.color = '#2d3036'
    window.add(u_head_2)

    u_head_3 = GPolygon()
    u_head_3.add_vertex((141, 301))
    u_head_3.add_vertex((150, 363))
    u_head_3.add_vertex((218, 323))
    u_head_3.add_vertex((175, 266))
    u_head_3.filled = True
    u_head_3.fill_color = '#21242a'
    u_head_3.color = '#21242a'
    window.add(u_head_3)

    u_head_4 = GPolygon()
    u_head_4.add_vertex((182, 240))
    u_head_4.add_vertex((175, 266))
    u_head_4.add_vertex((218, 323))
    u_head_4.add_vertex((247, 311))
    u_head_4.add_vertex((228, 217))
    u_head_4.filled = True
    u_head_4.fill_color = '#141b1c'
    u_head_4.color = '#141b1c'
    window.add(u_head_4)

    u_head_5 = GPolygon()
    u_head_5.add_vertex((228, 217))
    u_head_5.add_vertex((247, 311))
    u_head_5.add_vertex((253, 310))
    u_head_5.add_vertex((254, 290))
    u_head_5.add_vertex((261, 256))
    u_head_5.add_vertex((272, 290))
    u_head_5.add_vertex((273, 307))
    u_head_5.add_vertex((277, 306))
    u_head_5.add_vertex((288, 217))
    u_head_5.filled = True
    u_head_5.fill_color = '#434650'
    u_head_5.color = '#434650'
    window.add(u_head_5)

    u_head_6 = GPolygon()
    u_head_6.add_vertex((288, 217))
    u_head_6.add_vertex((277, 306))
    u_head_6.add_vertex((308, 320))
    u_head_6.add_vertex((344, 263))
    u_head_6.add_vertex((338, 237))
    u_head_6.filled = True
    u_head_6.fill_color = '#14191b'
    u_head_6.color = '#14191b'
    window.add(u_head_6)

    u_head_7 = GPolygon()
    u_head_7.add_vertex((344, 263))
    u_head_7.add_vertex((308, 320))
    u_head_7.add_vertex((376, 356))
    u_head_7.add_vertex((380, 288))
    u_head_7.filled = True
    u_head_7.fill_color = '#283039'
    u_head_7.color = '#283039'
    window.add(u_head_7)

    u_head_8 = GPolygon()
    u_head_8.add_vertex((380, 288))
    u_head_8.add_vertex((376, 356))
    u_head_8.add_vertex((381, 370))
    u_head_8.add_vertex((406, 359))
    u_head_8.add_vertex((425, 373))
    u_head_8.add_vertex((424, 300))
    u_head_8.filled = True
    u_head_8.fill_color = '#202932'
    u_head_8.color = '#202932'
    window.add(u_head_8)

    """
    This part is left face.
    """
    l_face_1 = GPolygon()
    l_face_1.add_vertex((95, 372))
    l_face_1.add_vertex((75, 411))
    l_face_1.add_vertex((89, 428))
    l_face_1.add_vertex((109, 447))
    l_face_1.filled = True
    l_face_1.fill_color = '#1d2022'
    l_face_1.color = '#1d2022'
    window.add(l_face_1)

    l_face_2 = GPolygon()
    l_face_2.add_vertex((89, 428))
    l_face_2.add_vertex((86, 469))
    l_face_2.add_vertex((104, 504))
    l_face_2.add_vertex((120, 496))
    l_face_2.add_vertex((109, 447))
    l_face_2.filled = True
    l_face_2.fill_color = '#1b1714'
    l_face_2.color = '#1b1714'
    window.add(l_face_2)

    l_face_3 = GPolygon()
    l_face_3.add_vertex((95, 372))
    l_face_3.add_vertex((109, 447))
    l_face_3.add_vertex((118, 385))
    l_face_3.filled = True
    l_face_3.fill_color = '#aeb4bb'
    l_face_3.color = '#aeb4bb'
    window.add(l_face_3)

    l_face_4 = GPolygon()
    l_face_4.add_vertex((109, 447))
    l_face_4.add_vertex((120, 496))
    l_face_4.add_vertex((157, 470))
    l_face_4.filled = True
    l_face_4.fill_color = '#d4d4d4'
    l_face_4.color = '#d4d4d4'
    window.add(l_face_4)

    l_face_5 = GPolygon()
    l_face_5.add_vertex((118, 385))
    l_face_5.add_vertex((109, 447))
    l_face_5.add_vertex((157, 470))
    l_face_5.add_vertex((170, 414))
    l_face_5.add_vertex((149, 386))
    l_face_5.filled = True
    l_face_5.fill_color = '#e0dfe1'
    l_face_5.color = '#e0dfe1'
    window.add(l_face_5)

    l_face_6 = GPolygon()
    l_face_6.add_vertex((118, 385))
    l_face_6.add_vertex((149, 386))
    l_face_6.add_vertex((150, 363))
    l_face_6.filled = True
    l_face_6.fill_color = '#6d7b84'
    l_face_6.color = '#6d7b84'
    window.add(l_face_6)

    l_face_7 = GPolygon()
    l_face_7.add_vertex((150, 363))
    l_face_7.add_vertex((149, 386))
    l_face_7.add_vertex((165, 378))
    l_face_7.add_vertex((172, 376))
    l_face_7.add_vertex((182, 370))
    l_face_7.add_vertex((197, 363))
    l_face_7.filled = True
    l_face_7.fill_color = '#dedee1'
    l_face_7.color = '#dedee1'
    window.add(l_face_7)

    l_face_8 = GPolygon()
    l_face_8.add_vertex((150, 363))
    l_face_8.add_vertex((197, 363))
    l_face_8.add_vertex((218, 323))
    l_face_8.filled = True
    l_face_8.fill_color = '#98a5b5'
    l_face_8.color = '#98a5b5'
    window.add(l_face_8)

    l_face_9 = GPolygon()
    l_face_9.add_vertex((149, 386))
    l_face_9.add_vertex((170, 414))
    l_face_9.add_vertex((179, 395))
    l_face_9.add_vertex((165, 378))
    l_face_9.filled = True
    l_face_9.fill_color = '#ccd1d7'
    l_face_9.color = '#ccd1d7'
    window.add(l_face_9)

    l_face_10 = GPolygon()
    l_face_10.add_vertex((165, 378))
    l_face_10.add_vertex((179, 395))
    l_face_10.add_vertex((180, 390))
    l_face_10.add_vertex((172, 376))
    l_face_10.filled = True
    l_face_10.fill_color = '#40454d'
    l_face_10.color = '#40454d'
    window.add(l_face_10)

    l_face_11 = GPolygon()
    l_face_11.add_vertex((172, 376))
    l_face_11.add_vertex((180, 390))
    l_face_11.add_vertex((187, 380))
    l_face_11.add_vertex((186, 373))
    l_face_11.add_vertex((193, 370))
    l_face_11.add_vertex((182, 370))
    l_face_11.filled = True
    l_face_11.fill_color = '#7eb0c4'
    l_face_11.color = '#7eb0c4'
    window.add(l_face_11)

    l_face_12 = GPolygon()
    l_face_12.add_vertex((186, 373))
    l_face_12.add_vertex((187, 380))
    l_face_12.add_vertex((196, 384))
    l_face_12.add_vertex((199, 374))
    l_face_12.add_vertex((193, 370))
    l_face_12.filled = True
    l_face_12.fill_color = '#0d1e3e'
    l_face_12.color = '#0d1e3e'
    window.add(l_face_12)

    l_face_13 = GPolygon()
    l_face_13.add_vertex((197, 363))
    l_face_13.add_vertex((193, 370))
    l_face_13.add_vertex((199, 374))
    l_face_13.add_vertex((204, 371))
    l_face_13.filled = True
    l_face_13.fill_color = '#b3b2b7'
    l_face_13.color = '#b3b2b7'
    window.add(l_face_13)

    l_face_14 = GPolygon()
    l_face_14.add_vertex((182, 370))
    l_face_14.add_vertex((193, 370))
    l_face_14.add_vertex((197, 363))
    l_face_14.filled = True
    l_face_14.fill_color = '#47535f'
    l_face_14.color = '#47535f'
    window.add(l_face_14)

    l_face_15 = GPolygon()
    l_face_15.add_vertex((187, 380))
    l_face_15.add_vertex((180, 390))
    l_face_15.add_vertex((198, 393))
    l_face_15.add_vertex((196, 384))
    l_face_15.filled = True
    l_face_15.fill_color = '#a0cbdd'
    l_face_15.color = '#a0cbdd'
    window.add(l_face_15)

    l_face_16 = GPolygon()
    l_face_16.add_vertex((180, 390))
    l_face_16.add_vertex((179, 395))
    l_face_16.add_vertex((197, 400))
    l_face_16.add_vertex((198, 393))
    l_face_16.filled = True
    l_face_16.fill_color = '#232b3a'
    l_face_16.color = '#232b3a'
    window.add(l_face_16)

    l_face_17 = GPolygon()
    l_face_17.add_vertex((198, 393))
    l_face_17.add_vertex((197, 400))
    l_face_17.add_vertex((213, 400))
    l_face_17.add_vertex((207, 388))
    l_face_17.filled = True
    l_face_17.fill_color = '#25262a'
    l_face_17.color = '#25262a'
    window.add(l_face_17)

    l_face_18 = GPolygon()
    l_face_18.add_vertex((199, 374))
    l_face_18.add_vertex((196, 384))
    l_face_18.add_vertex((198, 393))
    l_face_18.add_vertex((207, 388))
    l_face_18.filled = True
    l_face_18.fill_color = '#6894ab'
    l_face_18.color = '#6894ab'
    window.add(l_face_18)

    l_face_19 = GPolygon()
    l_face_19.add_vertex((199, 374))
    l_face_19.add_vertex((213, 400))
    l_face_19.add_vertex((216, 388))
    l_face_19.add_vertex((204, 371))
    l_face_19.filled = True
    l_face_19.fill_color = '#171d1d'
    l_face_19.color = '#171d1d'
    window.add(l_face_19)

    l_face_20 = GPolygon()
    l_face_20.add_vertex((218, 323))
    l_face_20.add_vertex((197, 363))
    l_face_20.add_vertex((204, 371))
    l_face_20.add_vertex((216, 388))
    l_face_20.add_vertex((240, 323))
    l_face_20.filled = True
    l_face_20.fill_color = '#c9d1d8'
    l_face_20.color = '#c9d1d8'
    window.add(l_face_20)

    l_face_21 = GPolygon()
    l_face_21.add_vertex((218, 323))
    l_face_21.add_vertex((240, 323))
    l_face_21.add_vertex((247, 311))
    l_face_21.filled = True
    l_face_21.fill_color = '#5d6772'
    l_face_21.color = '#5d6772'
    window.add(l_face_21)

    l_face_22 = GPolygon()
    l_face_22.add_vertex((240, 323))
    l_face_22.add_vertex((216, 388))
    l_face_22.add_vertex((228, 404))
    l_face_22.add_vertex((251, 381))
    l_face_22.filled = True
    l_face_22.fill_color = '#d3d6da'
    l_face_22.color = '#d3d6da'
    window.add(l_face_22)

    l_face_23 = GPolygon()
    l_face_23.add_vertex((240, 323))
    l_face_23.add_vertex((251, 381))
    l_face_23.add_vertex((253, 310))
    l_face_23.add_vertex((247, 311))
    l_face_23.filled = True
    l_face_23.fill_color = '#2f3135'
    l_face_23.color = '#2f3135'
    window.add(l_face_23)

    l_face_24 = GPolygon()
    l_face_24.add_vertex((261, 256))
    l_face_24.add_vertex((254, 290))
    l_face_24.add_vertex((253, 310))
    l_face_24.add_vertex((251, 381))
    l_face_24.add_vertex((280, 381))
    l_face_24.add_vertex((273, 307))
    l_face_24.add_vertex((272, 290))
    l_face_24.filled = True
    l_face_24.fill_color = '#cbcfd6'
    l_face_24.color = '#cbcfd6'
    window.add(l_face_24)

    l_face_25 = GPolygon()
    l_face_25.add_vertex((157, 470))
    l_face_25.add_vertex((184, 539))
    l_face_25.add_vertex((208, 441))
    l_face_25.add_vertex((170, 414))
    l_face_25.filled = True
    l_face_25.fill_color = '#e5e5e5'
    l_face_25.color = '#e5e5e5'
    window.add(l_face_25)

    l_face_26 = GPolygon()
    l_face_26.add_vertex((179, 395))
    l_face_26.add_vertex((170, 414))
    l_face_26.add_vertex((208, 441))
    l_face_26.add_vertex((212, 417))
    l_face_26.add_vertex((213, 400))
    l_face_26.add_vertex((197, 400))
    l_face_26.filled = True
    l_face_26.fill_color = '#b8c0cb'
    l_face_26.color = '#b8c0cb'
    window.add(l_face_26)

    l_face_27 = GPolygon()
    l_face_27.add_vertex((212, 417))
    l_face_27.add_vertex((208, 441))
    l_face_27.add_vertex((226, 418))
    l_face_27.filled = True
    l_face_27.fill_color = '#909dab'
    l_face_27.color = '#909dab'
    window.add(l_face_27)

    l_face_28 = GPolygon()
    l_face_28.add_vertex((216, 388))
    l_face_28.add_vertex((213, 400))
    l_face_28.add_vertex((212, 418))
    l_face_28.add_vertex((228, 404))
    l_face_28.filled = True
    l_face_28.fill_color = '#393d44'
    l_face_28.color = '#393d44'
    window.add(l_face_28)

    l_face_29 = GPolygon()
    l_face_29.add_vertex((228, 404))
    l_face_29.add_vertex((212, 417))
    l_face_29.add_vertex((226, 418))
    l_face_29.add_vertex((249, 419))
    l_face_29.filled = True
    l_face_29.fill_color = '#374351'
    l_face_29.color = '#374351'
    window.add(l_face_29)

    l_face_30 = GPolygon()
    l_face_30.add_vertex((228, 404))
    l_face_30.add_vertex((249, 419))
    l_face_30.add_vertex((251, 381))
    l_face_30.filled = True
    l_face_30.fill_color = '#434d5b'
    l_face_30.color = '#434d5b'
    window.add(l_face_30)

    l_face_31 = GPolygon()
    l_face_31.add_vertex((251, 381))
    l_face_31.add_vertex((249, 419))
    l_face_31.add_vertex((259, 391))
    l_face_31.filled = True
    l_face_31.fill_color = '#7b92a7'
    l_face_31.color = '#7b92a7'
    window.add(l_face_31)

    l_face_32 = GPolygon()
    l_face_32.add_vertex((251, 381))
    l_face_32.add_vertex((259, 391))
    l_face_32.add_vertex((273, 391))
    l_face_32.add_vertex((280, 381))
    l_face_32.filled = True
    l_face_32.fill_color = '#a9b9c6'
    l_face_32.color = '#a9b9c6'
    window.add(l_face_32)

    l_face_33 = GPolygon()
    l_face_33.add_vertex((208, 441))
    l_face_33.add_vertex((184, 539))
    l_face_33.add_vertex((204, 573))
    l_face_33.add_vertex((229, 539))
    l_face_33.add_vertex((229, 517))
    l_face_33.add_vertex((226, 418))
    l_face_33.filled = True
    l_face_33.fill_color = '#d8dde5'
    l_face_33.color = '#d8dde5'
    window.add(l_face_33)

    l_face_34 = GPolygon()
    l_face_34.add_vertex((226, 418))
    l_face_34.add_vertex((229, 517))
    l_face_34.add_vertex((255, 501))
    l_face_34.add_vertex((249, 419))
    l_face_34.filled = True
    l_face_34.fill_color = '#e9e9ec'
    l_face_34.color = '#e9e9ec'
    window.add(l_face_34)

    l_face_35 = GPolygon()
    l_face_35.add_vertex((259, 391))
    l_face_35.add_vertex((249, 419))
    l_face_35.add_vertex((255, 501))
    l_face_35.add_vertex((288, 502))
    l_face_35.add_vertex((283, 408))
    l_face_35.add_vertex((273, 391))
    l_face_35.filled = True
    l_face_35.fill_color = '#ccd1da'
    l_face_35.color = '#ccd1da'
    window.add(l_face_35)

    l_face_36 = GPolygon()
    l_face_36.add_vertex((229, 517))
    l_face_36.add_vertex((229, 539))
    l_face_36.add_vertex((235, 535))
    l_face_36.add_vertex((257, 522))
    l_face_36.add_vertex((255, 501))
    l_face_36.filled = True
    l_face_36.fill_color = '#7c93a2'
    l_face_36.color = '#7c93a2'
    window.add(l_face_36)

    l_face_37 = GPolygon()
    l_face_37.add_vertex((255, 501))
    l_face_37.add_vertex((257, 522))
    l_face_37.add_vertex((284, 522))
    l_face_37.add_vertex((288, 502))
    l_face_37.filled = True
    l_face_37.fill_color = '#3a4c61'
    l_face_37.color = '#3a4c61'
    window.add(l_face_37)

    l_face_38 = GPolygon()
    l_face_38.add_vertex((229, 539))
    l_face_38.add_vertex((204, 573))
    l_face_38.add_vertex((241, 578))
    l_face_38.add_vertex((247, 558))
    l_face_38.filled = True
    l_face_38.fill_color = '#b5bdc4'
    l_face_38.color = '#b5bdc4'
    window.add(l_face_38)

    l_face_39 = GPolygon()
    l_face_39.add_vertex((229, 539))
    l_face_39.add_vertex((247, 558))
    l_face_39.add_vertex((241, 543))
    l_face_39.add_vertex((235, 535))
    l_face_39.filled = True
    l_face_39.fill_color = '#4e555d'
    l_face_39.color = '#4e555d'
    window.add(l_face_39)

    l_face_40 = GPolygon()
    l_face_40.add_vertex((235, 535))
    l_face_40.add_vertex((241, 543))
    l_face_40.add_vertex((255, 544))
    l_face_40.add_vertex((264, 534))
    l_face_40.add_vertex((257, 522))
    l_face_40.filled = True
    l_face_40.fill_color = '#030d0c'
    l_face_40.color = '#030d0c'
    window.add(l_face_40)

    l_face_41 = GPolygon()
    l_face_41.add_vertex((257, 522))
    l_face_41.add_vertex((264, 534))
    l_face_41.add_vertex((282, 533))
    l_face_41.add_vertex((284, 522))
    l_face_41.filled = True
    l_face_41.fill_color = '#383533'
    l_face_41.color = '#383533'
    window.add(l_face_41)

    l_face_42 = GPolygon()
    l_face_42.add_vertex((241, 543))
    l_face_42.add_vertex((247, 558))
    l_face_42.add_vertex((261, 558))
    l_face_42.add_vertex((255, 544))
    l_face_42.filled = True
    l_face_42.fill_color = '#1a1a18'
    l_face_42.color = '#1a1a18'
    window.add(l_face_42)

    l_face_43 = GPolygon()
    l_face_43.add_vertex((264, 534))
    l_face_43.add_vertex((255, 544))
    l_face_43.add_vertex((285, 542))
    l_face_43.add_vertex((282, 533))
    l_face_43.filled = True
    l_face_43.fill_color = '#2b2926'
    l_face_43.color = '#2b2926'
    window.add(l_face_43)

    l_face_44 = GPolygon()
    l_face_44.add_vertex((255, 544))
    l_face_44.add_vertex((261, 558))
    l_face_44.add_vertex((277, 558))
    l_face_44.add_vertex((285, 542))
    l_face_44.filled = True
    l_face_44.fill_color = '#312c28'
    l_face_44.color = '#312c28'
    window.add(l_face_44)

    l_face_45 = GPolygon()
    l_face_45.add_vertex((247, 558))
    l_face_45.add_vertex((241, 578))
    l_face_45.add_vertex((268, 576))
    l_face_45.add_vertex((268, 566))
    l_face_45.add_vertex((261, 558))
    l_face_45.filled = True
    l_face_45.fill_color = '#4b565c'
    l_face_45.color = '#4b565c'
    window.add(l_face_45)

    l_face_46 = GPolygon()
    l_face_46.add_vertex((261, 558))
    l_face_46.add_vertex((268, 566))
    l_face_46.add_vertex((277, 558))
    l_face_46.filled = True
    l_face_46.fill_color = '#1f1d1b'
    l_face_46.color = '#1f1d1b'
    window.add(l_face_46)

    """
    This part is right face
    """
    r_face_1 = GPolygon()
    r_face_1.add_vertex((277, 306))
    r_face_1.add_vertex((273, 307))
    r_face_1.add_vertex((280, 381))
    r_face_1.add_vertex((283, 321))
    r_face_1.filled = True
    r_face_1.fill_color = '#54697a'
    r_face_1.color = '#54697a'
    window.add(r_face_1)

    r_face_2 = GPolygon()
    r_face_2.add_vertex((277, 306))
    r_face_2.add_vertex((283, 321))
    r_face_2.add_vertex((308, 320))
    r_face_2.filled = True
    r_face_2.fill_color = '#373f4a'
    r_face_2.color = '#373f4a'
    window.add(r_face_2)

    r_face_3 = GPolygon()
    r_face_3.add_vertex((283, 321))
    r_face_3.add_vertex((280, 381))
    r_face_3.add_vertex((304, 399))
    r_face_3.add_vertex((308, 320))
    r_face_3.filled = True
    r_face_3.fill_color = '#dddee0'
    r_face_3.color = '#dddee0'
    window.add(r_face_3)

    r_face_4 = GPolygon()
    r_face_4.add_vertex((308, 320))
    r_face_4.add_vertex((304, 399))
    r_face_4.add_vertex((315, 387))
    r_face_4.add_vertex((324, 342))
    r_face_4.filled = True
    r_face_4.fill_color = '#aeb7c3'
    r_face_4.color = '#aeb7c3'
    window.add(r_face_4)

    r_face_5 = GPolygon()
    r_face_5.add_vertex((324, 342))
    r_face_5.add_vertex((315, 387))
    r_face_5.add_vertex((331, 368))
    r_face_5.filled = True
    r_face_5.fill_color = '#a4afb9'
    r_face_5.color = '#a4afb9'
    window.add(r_face_5)

    r_face_6 = GPolygon()
    r_face_6.add_vertex((308, 320))
    r_face_6.add_vertex((324, 342))
    r_face_6.add_vertex((366, 361))
    r_face_6.add_vertex((376, 356))
    r_face_6.filled = True
    r_face_6.fill_color = '#2d414e'
    r_face_6.color = '#2d414e'
    window.add(r_face_6)

    r_face_7 = GPolygon()
    r_face_7.add_vertex((324, 342))
    r_face_7.add_vertex((331, 368))
    r_face_7.add_vertex((354, 373))
    r_face_7.add_vertex((366, 361))
    r_face_7.filled = True
    r_face_7.fill_color = '#a8b4c5'
    r_face_7.color = '#a8b4c5'
    window.add(r_face_7)

    r_face_8 = GPolygon()
    r_face_8.add_vertex((354, 373))
    r_face_8.add_vertex((357, 376))
    r_face_8.add_vertex((378, 383))
    r_face_8.add_vertex((366, 361))
    r_face_8.filled = True
    r_face_8.fill_color = '#6c818e'
    r_face_8.color = '#6c818e'
    window.add(r_face_8)

    r_face_9 = GPolygon()
    r_face_9.add_vertex((366, 361))
    r_face_9.add_vertex((378, 383))
    r_face_9.add_vertex((381, 370))
    r_face_9.add_vertex((376, 356))
    r_face_9.filled = True
    r_face_9.fill_color = '#7da1b9'
    r_face_9.color = '#7da1b9'
    window.add(r_face_9)

    r_face_10 = GPolygon()
    r_face_10.add_vertex((381, 370))
    r_face_10.add_vertex((378, 383))
    r_face_10.add_vertex((407, 382))
    r_face_10.add_vertex((406, 359))
    r_face_10.filled = True
    r_face_10.fill_color = '#495d67'
    r_face_10.color = '#495d67'
    window.add(r_face_10)

    r_face_11 = GPolygon()
    r_face_11.add_vertex((406, 359))
    r_face_11.add_vertex((407, 382))
    r_face_11.add_vertex((417, 387))
    r_face_11.add_vertex((426, 373))
    r_face_11.filled = True
    r_face_11.fill_color = '#7591a0'
    r_face_11.color = '#7591a0'
    window.add(r_face_11)

    r_face_12 = GPolygon()
    r_face_12.add_vertex((280, 381))
    r_face_12.add_vertex((273, 391))
    r_face_12.add_vertex((283, 408))
    r_face_12.add_vertex((304, 399))
    r_face_12.filled = True
    r_face_12.fill_color = '#5c6c79'
    r_face_12.color = '#5c6c79'
    window.add(r_face_12)

    r_face_13 = GPolygon()
    r_face_13.add_vertex((304, 399))
    r_face_13.add_vertex((283, 408))
    r_face_13.add_vertex((299, 410))
    r_face_13.add_vertex((316, 416))
    r_face_13.filled = True
    r_face_13.fill_color = '#283848'
    r_face_13.color = '#283848'
    window.add(r_face_13)

    r_face_14 = GPolygon()
    r_face_14.add_vertex((304, 399))
    r_face_14.add_vertex((316, 416))
    r_face_14.add_vertex((317, 402))
    r_face_14.add_vertex((315, 387))
    r_face_14.filled = True
    r_face_14.fill_color = '#50595f'
    r_face_14.color = '#50595f'
    window.add(r_face_14)

    r_face_15 = GPolygon()
    r_face_15.add_vertex((331, 368))
    r_face_15.add_vertex((315, 387))
    r_face_15.add_vertex((317, 402))
    r_face_15.add_vertex((354, 391))
    r_face_15.add_vertex((350, 387))
    r_face_15.add_vertex((333, 392))
    r_face_15.add_vertex((323, 388))
    r_face_15.add_vertex((332, 373))
    r_face_15.add_vertex((341, 372))
    r_face_15.add_vertex((348, 372))
    r_face_15.add_vertex((354, 373))
    r_face_15.filled = True
    r_face_15.fill_color = '#181d1d'
    r_face_15.color = '#181d1d'
    window.add(r_face_15)

    r_face_16 = GPolygon()
    r_face_16.add_vertex((332, 373))
    r_face_16.add_vertex((323, 388))
    r_face_16.add_vertex((331, 380))
    r_face_16.filled = True
    r_face_16.fill_color = '#a4d2f2'
    r_face_16.color = '#a4d2f2'
    window.add(r_face_16)

    r_face_17 = GPolygon()
    r_face_17.add_vertex((332, 373))
    r_face_17.add_vertex((331, 380))
    r_face_17.add_vertex((335, 384))
    r_face_17.add_vertex((342, 380))
    r_face_17.add_vertex((341, 373))
    r_face_17.filled = True
    r_face_17.fill_color = '#0d1e3e'
    r_face_17.color = '#0d1e3e'
    window.add(r_face_17)

    r_face_18 = GPolygon()
    r_face_18.add_vertex((331, 380))
    r_face_18.add_vertex((323, 388))
    r_face_18.add_vertex((333, 392))
    r_face_18.add_vertex((335, 384))
    r_face_18.filled = True
    r_face_18.fill_color = '#4196aa'
    r_face_18.color = '#4196aa'
    window.add(r_face_18)

    r_face_19 = GPolygon()
    r_face_19.add_vertex((335, 384))
    r_face_19.add_vertex((333, 392))
    r_face_19.add_vertex((350, 387))
    r_face_19.add_vertex((342, 380))
    r_face_19.filled = True
    r_face_19.fill_color = '#86d0e3'
    r_face_19.color = '#86d0e3'
    window.add(r_face_19)

    r_face_20 = GPolygon()
    r_face_20.add_vertex((341, 373))
    r_face_20.add_vertex((342, 380))
    r_face_20.add_vertex((350, 387))
    r_face_20.add_vertex((348, 372))
    r_face_20.filled = True
    r_face_20.fill_color = '#60a6b8'
    r_face_20.color = '#60a6b8'
    window.add(r_face_20)

    r_face_21 = GPolygon()
    r_face_21.add_vertex((348, 372))
    r_face_21.add_vertex((350, 387))
    r_face_21.add_vertex((357, 376))
    r_face_21.add_vertex((354, 373))
    r_face_21.filled = True
    r_face_21.fill_color = '#091011'
    r_face_21.color = '#091011'
    window.add(r_face_21)

    r_face_22 = GPolygon()
    r_face_22.add_vertex((357, 376))
    r_face_22.add_vertex((350, 387))
    r_face_22.add_vertex((354, 391))
    r_face_22.add_vertex((363, 378))
    r_face_22.filled = True
    r_face_22.fill_color = '#27343f'
    r_face_22.color = '#27343f'
    window.add(r_face_22)

    r_face_23 = GPolygon()
    r_face_23.add_vertex((283, 408))
    r_face_23.add_vertex((288, 502))
    r_face_23.add_vertex((306, 517))
    r_face_23.add_vertex((299, 410))
    r_face_23.filled = True
    r_face_23.fill_color = '#d4dae1'
    r_face_23.color = '#d4dae1'
    window.add(r_face_23)

    r_face_24 = GPolygon()
    r_face_24.add_vertex((299, 410))
    r_face_24.add_vertex((306, 517))
    r_face_24.add_vertex((307, 537))
    r_face_24.add_vertex((330, 563))
    r_face_24.add_vertex((342, 524))
    r_face_24.add_vertex((319, 442))
    r_face_24.filled = True
    r_face_24.fill_color = '#c4d1db'
    r_face_24.color = '#c4d1db'
    window.add(r_face_24)

    r_face_25 = GPolygon()
    r_face_25.add_vertex((299, 410))
    r_face_25.add_vertex((319, 442))
    r_face_25.add_vertex((316, 416))
    r_face_25.filled = True
    r_face_25.fill_color = '#526575'
    r_face_25.color = '#526575'
    window.add(r_face_25)

    r_face_26 = GPolygon()
    r_face_26.add_vertex((317, 402))
    r_face_26.add_vertex((316, 416))
    r_face_26.add_vertex((319, 442))
    r_face_26.add_vertex((351, 420))
    r_face_26.filled = True
    r_face_26.fill_color = '#beceda'
    r_face_26.color = '#beceda'
    window.add(r_face_26)

    r_face_27 = GPolygon()
    r_face_27.add_vertex((317, 402))
    r_face_27.add_vertex((351, 420))
    r_face_27.add_vertex((354, 391))
    r_face_27.filled = True
    r_face_27.fill_color = '#b4c3ce'
    r_face_27.color = '#b4c3ce'
    window.add(r_face_27)

    r_face_28 = GPolygon()
    r_face_28.add_vertex((354, 391))
    r_face_28.add_vertex((351, 420))
    r_face_28.add_vertex((377, 408))
    r_face_28.add_vertex((378, 383))
    r_face_28.add_vertex((363, 378))
    r_face_28.filled = True
    r_face_28.fill_color = '#a8bcca'
    r_face_28.color = '#a8bcca'
    window.add(r_face_28)

    r_face_29 = GPolygon()
    r_face_29.add_vertex((378, 383))
    r_face_29.add_vertex((377, 408))
    r_face_29.add_vertex((405, 455))
    r_face_29.add_vertex((407, 382))
    r_face_29.filled = True
    r_face_29.fill_color = '#d0d8de'
    r_face_29.color = '#d0d8de'
    window.add(r_face_29)

    r_face_30 = GPolygon()
    r_face_30.add_vertex((407, 382))
    r_face_30.add_vertex((405, 455))
    r_face_30.add_vertex((419, 441))
    r_face_30.add_vertex((417, 387))
    r_face_30.filled = True
    r_face_30.fill_color = '#bfccd3'
    r_face_30.color = '#bfccd3'
    window.add(r_face_30)

    r_face_31 = GPolygon()
    r_face_31.add_vertex((417, 387))
    r_face_31.add_vertex((419, 441))
    r_face_31.add_vertex((445, 414))
    r_face_31.add_vertex((425, 373))
    r_face_31.filled = True
    r_face_31.fill_color = '#1b2326'
    r_face_31.color = '#1b2326'
    window.add(r_face_31)

    r_face_32 = GPolygon()
    r_face_32.add_vertex((319, 442))
    r_face_32.add_vertex((342, 524))
    r_face_32.add_vertex((367, 474))
    r_face_32.add_vertex((351, 420))
    r_face_32.filled = True
    r_face_32.fill_color = '#cdd7de'
    r_face_32.color = '#cdd7de'
    window.add(r_face_32)

    r_face_33 = GPolygon()
    r_face_33.add_vertex((367, 474))
    r_face_33.add_vertex((342, 524))
    r_face_33.add_vertex((386, 523))
    r_face_33.filled = True
    r_face_33.fill_color = '#b8c1c6'
    r_face_33.color = '#b8c1c6'
    window.add(r_face_33)

    r_face_34 = GPolygon()
    r_face_34.add_vertex((351, 420))
    r_face_34.add_vertex((367, 474))
    r_face_34.add_vertex((386, 523))
    r_face_34.add_vertex((401, 490))
    r_face_34.add_vertex((405, 455))
    r_face_34.add_vertex((377, 408))
    r_face_34.filled = True
    r_face_34.fill_color = '#becbd1'
    r_face_34.color = '#becbd1'
    window.add(r_face_34)

    r_face_35 = GPolygon()
    r_face_35.add_vertex((405, 455))
    r_face_35.add_vertex((401, 490))
    r_face_35.add_vertex((423, 488))
    r_face_35.add_vertex((419, 441))
    r_face_35.filled = True
    r_face_35.fill_color = '#627f8e'
    r_face_35.color = '#627f8e'
    window.add(r_face_35)

    r_face_36 = GPolygon()
    r_face_36.add_vertex((419, 441))
    r_face_36.add_vertex((423, 488))
    r_face_36.add_vertex((445, 414))
    r_face_36.filled = True
    r_face_36.fill_color = '#1d1f1d'
    r_face_36.color = '#1d1f1d'
    window.add(r_face_36)

    r_face_37 = GPolygon()
    r_face_37.add_vertex((288, 502))
    r_face_37.add_vertex((284, 522))
    r_face_37.add_vertex((302, 535))
    r_face_37.add_vertex((307, 537))
    r_face_37.add_vertex((306, 517))
    r_face_37.filled = True
    r_face_37.fill_color = '#5c7d91'
    r_face_37.color = '#5c7d91'
    window.add(r_face_37)

    r_face_38 = GPolygon()
    r_face_38.add_vertex((284, 522))
    r_face_38.add_vertex((282, 533))
    r_face_38.add_vertex((285, 542))
    r_face_38.add_vertex((296, 542))
    r_face_38.add_vertex((302, 535))
    r_face_38.filled = True
    r_face_38.fill_color = '#030d0c'
    r_face_38.color = '#030d0c'
    window.add(r_face_38)

    r_face_39 = GPolygon()
    r_face_39.add_vertex((285, 542))
    r_face_39.add_vertex((277, 558))
    r_face_39.add_vertex((295, 556))
    r_face_39.add_vertex((296, 542))
    r_face_39.filled = True
    r_face_39.fill_color = '#1a1a1a'
    r_face_39.color = '#1a1a1a'
    window.add(r_face_39)

    r_face_40 = GPolygon()
    r_face_40.add_vertex((296, 542))
    r_face_40.add_vertex((295, 556))
    r_face_40.add_vertex((307, 537))
    r_face_40.add_vertex((302, 535))
    r_face_40.filled = True
    r_face_40.fill_color = '#485a63'
    r_face_40.color = '#485a63'
    window.add(r_face_40)

    r_face_41 = GPolygon()
    r_face_41.add_vertex((277, 558))
    r_face_41.add_vertex((268, 566))
    r_face_41.add_vertex((268, 576))
    r_face_41.add_vertex((301, 576))
    r_face_41.add_vertex((295, 556))
    r_face_41.filled = True
    r_face_41.fill_color = '#64747e'
    r_face_41.color = '#64747e'
    window.add(r_face_41)

    r_face_42 = GPolygon()
    r_face_42.add_vertex((295, 556))
    r_face_42.add_vertex((301, 576))
    r_face_42.add_vertex((330, 563))
    r_face_42.add_vertex((307, 537))
    r_face_42.filled = True
    r_face_42.fill_color = '#a2b6c5'
    r_face_42.color = '#a2b6c5'
    window.add(r_face_42)

    """
    This part is body
    """
    body_1 = GPolygon()
    body_1.add_vertex((113, 572))
    body_1.add_vertex((102, 589))
    body_1.add_vertex((95, 682))
    body_1.add_vertex((124, 681))
    body_1.add_vertex((119, 609))
    body_1.filled = True
    body_1.fill_color = '#2a211d'
    body_1.color = '#2a211d'
    window.add(body_1)

    body_2 = GPolygon()
    body_2.add_vertex((120, 496))
    body_2.add_vertex((104, 504))
    body_2.add_vertex((113, 572))
    body_2.add_vertex((119, 609))
    body_2.add_vertex((178, 632))
    body_2.add_vertex((184, 595))
    body_2.add_vertex((169, 565))
    body_2.filled = True
    body_2.fill_color = '#090f0e'
    body_2.color = '#090f0e'
    window.add(body_2)

    body_3 = GPolygon()
    body_3.add_vertex((120, 496))
    body_3.add_vertex((169, 565))
    body_3.add_vertex((184, 539))
    body_3.add_vertex((157, 470))
    body_3.filled = True
    body_3.fill_color = '#c7c5c5'
    body_3.color = '#c7c5c5'
    window.add(body_3)

    body_4 = GPolygon()
    body_4.add_vertex((184, 539))
    body_4.add_vertex((169, 565))
    body_4.add_vertex((184, 595))
    body_4.add_vertex((204, 573))
    body_4.filled = True
    body_4.fill_color = '#c7c5c5'
    body_4.color = '#c7c5c5'
    window.add(body_4)

    body_4 = GPolygon()
    body_4.add_vertex((184, 539))
    body_4.add_vertex((169, 565))
    body_4.add_vertex((184, 595))
    body_4.add_vertex((204, 573))
    body_4.filled = True
    body_4.fill_color = '#c7c5c5'
    body_4.color = '#c7c5c5'
    window.add(body_4)

    body_5 = GPolygon()
    body_5.add_vertex((119, 609))
    body_5.add_vertex((124, 681))
    body_5.add_vertex((196, 656))
    body_5.add_vertex((178, 632))
    body_5.filled = True
    body_5.fill_color = '#cdced3'
    body_5.color = '#cdced3'
    window.add(body_5)

    body_6 = GPolygon()
    body_6.add_vertex((178, 632))
    body_6.add_vertex((196, 656))
    body_6.add_vertex((223, 623))
    body_6.add_vertex((184, 595))
    body_6.filled = True
    body_6.fill_color = '#999e98'
    body_6.color = '#999e98'
    window.add(body_6)

    body_7 = GPolygon()
    body_7.add_vertex((184, 595))
    body_7.add_vertex((223, 623))
    body_7.add_vertex((249, 591))
    body_7.add_vertex((241, 578))
    body_7.add_vertex((204, 573))
    body_7.filled = True
    body_7.fill_color = '#aaa69d'
    body_7.color = '#aaa69d'
    window.add(body_7)

    body_7 = GPolygon()
    body_7.add_vertex((184, 595))
    body_7.add_vertex((223, 623))
    body_7.add_vertex((249, 591))
    body_7.add_vertex((241, 578))
    body_7.add_vertex((204, 573))
    body_7.filled = True
    body_7.fill_color = '#aaa69d'
    body_7.color = '#aaa69d'
    window.add(body_7)

    body_8 = GPolygon()
    body_8.add_vertex((95, 682))
    body_8.add_vertex((98, 706))
    body_8.add_vertex((134, 706))
    body_8.add_vertex((124, 681))
    body_8.filled = True
    body_8.fill_color = '#443d3c'
    body_8.color = '#443d3c'
    window.add(body_8)

    body_8 = GPolygon()
    body_8.add_vertex((95, 682))
    body_8.add_vertex((98, 706))
    body_8.add_vertex((134, 706))
    body_8.add_vertex((124, 681))
    body_8.filled = True
    body_8.fill_color = '#443d3c'
    body_8.color = '#443d3c'
    window.add(body_8)

    body_9 = GPolygon()
    body_9.add_vertex((124, 681))
    body_9.add_vertex((134, 706))
    body_9.add_vertex((198, 706))
    body_9.add_vertex((196, 656))
    body_9.filled = True
    body_9.fill_color = '#b3b3b5'
    body_9.color = '#b3b3b5'
    window.add(body_9)

    body_10 = GPolygon()
    body_10.add_vertex((196, 656))
    body_10.add_vertex((198, 706))
    body_10.add_vertex((241, 684))
    body_10.add_vertex((223, 623))
    body_10.filled = True
    body_10.fill_color = '#a2a49e'
    body_10.color = '#a2a49e'
    window.add(body_10)

    body_11 = GPolygon()
    body_11.add_vertex((223, 623))
    body_11.add_vertex((241, 684))
    body_11.add_vertex((307, 629))
    body_11.add_vertex((291, 591))
    body_11.add_vertex((249, 591))
    body_11.filled = True
    body_11.fill_color = '#babcbc'
    body_11.color = '#babcbc'
    window.add(body_11)

    body_12 = GPolygon()
    body_12.add_vertex((241, 578))
    body_12.add_vertex((249, 591))
    body_12.add_vertex((291, 591))
    body_12.add_vertex((301, 576))
    body_12.filled = True
    body_12.fill_color = '#7a7266'
    body_12.color = '#7a7266'
    window.add(body_12)

    body_13 = GPolygon()
    body_13.add_vertex((257, 577))
    body_13.add_vertex((267, 582))
    body_13.add_vertex((277, 576))
    body_13.filled = True
    body_13.fill_color = '#383533'
    body_13.color = '#383533'
    window.add(body_13)

    body_14 = GPolygon()
    body_14.add_vertex((241, 684))
    body_14.add_vertex((307, 669))
    body_14.add_vertex((307, 629))
    body_14.filled = True
    body_14.fill_color = '#939da1'
    body_14.color = '#939da1'
    window.add(body_14)

    body_14 = GPolygon()
    body_14.add_vertex((241, 684))
    body_14.add_vertex((307, 669))
    body_14.add_vertex((307, 629))
    body_14.filled = True
    body_14.fill_color = '#939da1'
    body_14.color = '#939da1'
    window.add(body_14)

    body_15 = GPolygon()
    body_15.add_vertex((401, 490))
    body_15.add_vertex((386, 523))
    body_15.add_vertex((335, 584))
    body_15.add_vertex((307, 629))
    body_15.add_vertex((307, 669))
    body_15.add_vertex((241, 684))
    body_15.add_vertex((198, 706))
    body_15.add_vertex((421, 706))
    body_15.add_vertex((370, 639))
    body_15.add_vertex((414, 550))
    body_15.add_vertex((423, 488))
    body_15.filled = True
    body_15.fill_color = '#09100f'
    body_15.color = '#09100f'
    window.add(body_15)

    body_16 = GPolygon()
    body_16.add_vertex((330, 563))
    body_16.add_vertex((301, 576))
    body_16.add_vertex((291, 591))
    body_16.add_vertex((307, 629))
    body_16.add_vertex((335, 584))
    body_16.filled = True
    body_16.fill_color = '#a9aead'
    body_16.color = '#a9aead'
    window.add(body_16)

    body_17 = GPolygon()
    body_17.add_vertex((330, 563))
    body_17.add_vertex((335, 584))
    body_17.add_vertex((386, 523))
    body_17.add_vertex((342, 524))
    body_17.filled = True
    body_17.fill_color = '#a0abae'
    body_17.color = '#a0abae'
    window.add(body_17)

    body_18 = GPolygon()
    body_18.add_vertex((414, 550))
    body_18.add_vertex((370, 639))
    body_18.add_vertex((421, 706))
    body_18.add_vertex((429, 616))
    body_18.filled = True
    body_18.fill_color = '#121716'
    body_18.color = '#121716'
    window.add(body_18)

    body_19 = GPolygon()
    body_19.add_vertex((429, 616))
    body_19.add_vertex((421, 706))
    body_19.add_vertex((468, 706))
    body_19.filled = True
    body_19.fill_color = '#1f252b'
    body_19.color = '#1f252b'
    window.add(body_19)

    body_20 = GPolygon()
    body_20.add_vertex((485, 536))
    body_20.add_vertex((429, 616))
    body_20.add_vertex((468, 706))
    body_20.add_vertex((499, 587))
    body_20.filled = True
    body_20.fill_color = '#2c313c'
    body_20.color = '#2c313c'
    window.add(body_20)

    body_21 = GPolygon()
    body_21.add_vertex((499, 587))
    body_21.add_vertex((468, 706))
    body_21.add_vertex((499, 706))
    body_21.filled = True
    body_21.fill_color = '#0e1314'
    body_21.color = '#0e1314'
    window.add(body_21)

    body_22 = GPolygon()
    body_22.add_vertex((423, 488))
    body_22.add_vertex((414, 550))
    body_22.add_vertex((429, 616))
    body_22.add_vertex((485, 536))
    body_22.filled = True
    body_22.fill_color = '#3c414b'
    body_22.color = '#3c414b'
    window.add(body_22)

    body_23 = GPolygon()
    body_23.add_vertex((423, 488))
    body_23.add_vertex((485, 536))
    body_23.add_vertex((457, 451))
    body_23.add_vertex((435, 447))
    body_23.filled = True
    body_23.fill_color = '#494d59'
    body_23.color = '#494d59'
    window.add(body_23)

    body_24 = GPolygon()
    body_24.add_vertex((457, 451))
    body_24.add_vertex((485, 536))
    body_24.add_vertex((499, 587))
    body_24.add_vertex((499, 446))
    body_24.filled = True
    body_24.fill_color = '#323239'
    body_24.color = '#323239'
    window.add(body_24)



if __name__ == '__main__':
    main()
