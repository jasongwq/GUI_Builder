#include "UI.h"
Window window0(0);
Button Button0_1;
Button Button0_2;
Button Button0_3;
Button Button0_4;
Button Button0_5;
Button Button0_6;
Window window1(1);
Button Button1_1;
Window window2(2);
Button Button2_1;
Window window3(3);
Button Button3_1;
Window window4(4);
Button Button4_1;
Window window5(5);
Button Button5_1;
Window window6(6);
Button Button6_1;
Window window7(7);
Button Button7_1;
Window window8(8);
Button Button8_1;
#include "UI.h"
Window window0(0);
Button Button0_1;
Button Button0_2;
Button Button0_3;
Button Button0_4;
Button Button0_5;
Button Button0_6;
Button Button0_7;
Window window1(1);
Button Button1_1;
Window window2(2);
Button Button2_1;
Window window3(3);
Button Button3_1;
Window window4(4);
Button Button4_1;
Window window5(5);
Button Button5_1;
Window window6(6);
Button Button6_1;
Window window7(7);
Button Button7_1;
Window window8(8);
Button Button8_1;
int Button0_1_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_2_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_3_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_4_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_5_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_6_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button1_1_Event(Event event){
if (event == press){window1.Refresh();}return 0;}
int Button2_1_Event(Event event){
if (event == press){window2.Refresh();}return 0;}
int Button3_1_Event(Event event){
if (event == press){window3.Refresh();}return 0;}
int Button4_1_Event(Event event){
if (event == press){window4.Refresh();}return 0;}
int Button5_1_Event(Event event){
if (event == press){window5.Refresh();}return 0;}
int Button6_1_Event(Event event){
if (event == press){window6.Refresh();}return 0;}
int Button7_1_Event(Event event){
if (event == press){window7.Refresh();}return 0;}
int Button8_1_Event(Event event){
if (event == press){window8.Refresh();}return 0;}
int Button0_1_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_2_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_3_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_4_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_5_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_6_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button0_7_Event(Event event){
if (event == press){window0.Refresh();}return 0;}
int Button1_1_Event(Event event){
if (event == press){window1.Refresh();}return 0;}
int Button2_1_Event(Event event){
if (event == press){window2.Refresh();}return 0;}
int Button3_1_Event(Event event){
if (event == press){window3.Refresh();}return 0;}
int Button4_1_Event(Event event){
if (event == press){window4.Refresh();}return 0;}
int Button5_1_Event(Event event){
if (event == press){window5.Refresh();}return 0;}
int Button6_1_Event(Event event){
if (event == press){window6.Refresh();}return 0;}
int Button7_1_Event(Event event){
if (event == press){window7.Refresh();}return 0;}
int Button8_1_Event(Event event){
if (event == press){window8.Refresh();}return 0;}
void UI_Init(void){
ui.add_window(&window0);
window0.Set_BackColor(0xfe38);
window0.Set_Rect(0,0,240,320);
window0.add_button(&Button0_1);
Button0_1.rect.Set_Rect(20,30,80,80);
Button0_1.text.Set_Text((char *)"ceshi");
Button0_1.Set_Event(&Button0_1_Event);
window0.add_button(&Button0_2);
Button0_2.rect.Set_Rect(140,30,80,80);
Button0_2.text.Set_Text((char *)"ceshi");
Button0_2.Set_Event(&Button0_2_Event);
window0.add_button(&Button0_3);
Button0_3.rect.Set_Rect(140,130,80,80);
Button0_3.text.Set_Text((char *)"ceshi");
Button0_3.Set_Event(&Button0_3_Event);
window0.add_button(&Button0_4);
Button0_4.rect.Set_Rect(140,230,80,80);
Button0_4.text.Set_Text((char *)"ceshi");
Button0_4.Set_Event(&Button0_4_Event);
window0.add_button(&Button0_5);
Button0_5.rect.Set_Rect(20,230,80,80);
Button0_5.text.Set_Text((char *)"ceshi");
Button0_5.Set_Event(&Button0_5_Event);
window0.add_button(&Button0_6);
Button0_6.rect.Set_Rect(20,130,80,80);
Button0_6.text.Set_Text((char *)"ceshi");
Button0_6.Set_Event(&Button0_6_Event);
ui.add_window(&window1);
window1.Set_BackColor(0x7b7f);
window1.Set_Rect(0,0,240,320);
window1.add_button(&Button1_1);
Button1_1.rect.Set_Rect(0,0,240,15);
Button1_1.text.Set_Text((char *)"ceshi");
Button1_1.Set_Event(&Button1_1_Event);
ui.add_window(&window2);
window2.Set_BackColor(0xfd36);
window2.Set_Rect(0,0,240,320);
window2.add_button(&Button2_1);
Button2_1.rect.Set_Rect(0,0,240,15);
Button2_1.text.Set_Text((char *)"ceshi");
Button2_1.Set_Event(&Button2_1_Event);
ui.add_window(&window3);
window3.Set_BackColor(0xf69f);
window3.Set_Rect(0,0,240,320);
window3.add_button(&Button3_1);
Button3_1.rect.Set_Rect(0,0,240,15);
Button3_1.text.Set_Text((char *)"ceshi");
Button3_1.Set_Event(&Button3_1_Event);
ui.add_window(&window4);
window4.Set_BackColor(0xc7fc);
window4.Set_Rect(0,0,240,320);
window4.add_button(&Button4_1);
Button4_1.rect.Set_Rect(0,0,240,15);
Button4_1.text.Set_Text((char *)"ceshi");
Button4_1.Set_Event(&Button4_1_Event);
ui.add_window(&window5);
window5.Set_BackColor(0xd7f9);
window5.Set_Rect(0,0,240,320);
window5.add_button(&Button5_1);
Button5_1.rect.Set_Rect(0,0,240,15);
Button5_1.text.Set_Text((char *)"ceshi");
Button5_1.Set_Event(&Button5_1_Event);
ui.add_window(&window6);
window6.Set_BackColor(0xaffc);
window6.Set_Rect(0,0,240,320);
window6.add_button(&Button6_1);
Button6_1.rect.Set_Rect(0,0,240,15);
Button6_1.text.Set_Text((char *)"ceshi");
Button6_1.Set_Event(&Button6_1_Event);
ui.add_window(&window7);
window7.Set_BackColor(0xfff2);
window7.Set_Rect(0,0,240,320);
window7.add_button(&Button7_1);
Button7_1.rect.Set_Rect(0,0,240,15);
Button7_1.text.Set_Text((char *)"ceshi");
Button7_1.Set_Event(&Button7_1_Event);
ui.add_window(&window8);
window8.Set_BackColor(0xf8e0);
window8.Set_Rect(0,0,240,320);
window8.add_button(&Button8_1);
Button8_1.rect.Set_Rect(90,100,100,100);
Button8_1.text.Set_Text((char *)"ceshi");
Button8_1.Set_Event(&Button8_1_Event);
window0.Refresh();
}
void UI_Init(void){
ui.add_window(&window0);
window0.Set_BackColor(0xfe38);
window0.Set_Rect(0,0,240,320);
window0.add_button(&Button0_1);
Button0_1.rect.Set_Rect(20,30,80,80);
Button0_1.text.Set_Text((char *)"ceshi");
Button0_1.Set_Event(&Button0_1_Event);
window0.add_button(&Button0_2);
Button0_2.rect.Set_Rect(140,30,80,80);
Button0_2.text.Set_Text((char *)"ceshi");
Button0_2.Set_Event(&Button0_2_Event);
window0.add_button(&Button0_3);
Button0_3.rect.Set_Rect(140,130,80,80);
Button0_3.text.Set_Text((char *)"ceshi");
Button0_3.Set_Event(&Button0_3_Event);
window0.add_button(&Button0_4);
Button0_4.rect.Set_Rect(140,230,80,80);
Button0_4.text.Set_Text((char *)"ceshi");
Button0_4.Set_Event(&Button0_4_Event);
window0.add_button(&Button0_5);
Button0_5.rect.Set_Rect(20,230,80,80);
Button0_5.text.Set_Text((char *)"ceshi");
Button0_5.Set_Event(&Button0_5_Event);
window0.add_button(&Button0_6);
Button0_6.rect.Set_Rect(20,130,80,80);
Button0_6.text.Set_Text((char *)"ceshi");
Button0_6.Set_Event(&Button0_6_Event);
window0.add_button(&Button0_7);
Button0_7.rect.Set_Rect(0,0,240,25);
Button0_7.text.Set_Text((char *)"ceshi");
Button0_7.Set_Event(&Button0_7_Event);
ui.add_window(&window1);
window1.Set_BackColor(0x7b7f);
window1.Set_Rect(0,0,240,320);
window1.add_button(&Button1_1);
Button1_1.rect.Set_Rect(0,0,240,25);
Button1_1.text.Set_Text((char *)"ceshi");
Button1_1.Set_Event(&Button1_1_Event);
ui.add_window(&window2);
window2.Set_BackColor(0xfd36);
window2.Set_Rect(0,0,240,320);
window2.add_button(&Button2_1);
Button2_1.rect.Set_Rect(0,0,240,25);
Button2_1.text.Set_Text((char *)"ceshi");
Button2_1.Set_Event(&Button2_1_Event);
ui.add_window(&window3);
window3.Set_BackColor(0xf69f);
window3.Set_Rect(0,0,240,320);
window3.add_button(&Button3_1);
Button3_1.rect.Set_Rect(0,0,240,25);
Button3_1.text.Set_Text((char *)"ceshi");
Button3_1.Set_Event(&Button3_1_Event);
ui.add_window(&window4);
window4.Set_BackColor(0xc7fc);
window4.Set_Rect(0,0,240,320);
window4.add_button(&Button4_1);
Button4_1.rect.Set_Rect(0,0,240,25);
Button4_1.text.Set_Text((char *)"ceshi");
Button4_1.Set_Event(&Button4_1_Event);
ui.add_window(&window5);
window5.Set_BackColor(0xd7f9);
window5.Set_Rect(0,0,240,320);
window5.add_button(&Button5_1);
Button5_1.rect.Set_Rect(0,0,240,25);
Button5_1.text.Set_Text((char *)"ceshi");
Button5_1.Set_Event(&Button5_1_Event);
ui.add_window(&window6);
window6.Set_BackColor(0xaffc);
window6.Set_Rect(0,0,240,320);
window6.add_button(&Button6_1);
Button6_1.rect.Set_Rect(0,0,240,25);
Button6_1.text.Set_Text((char *)"ceshi");
Button6_1.Set_Event(&Button6_1_Event);
ui.add_window(&window7);
window7.Set_BackColor(0xfff2);
window7.Set_Rect(0,0,240,320);
window7.add_button(&Button7_1);
Button7_1.rect.Set_Rect(0,0,240,25);
Button7_1.text.Set_Text((char *)"ceshi");
Button7_1.Set_Event(&Button7_1_Event);
ui.add_window(&window8);
window8.Set_BackColor(0xf8e0);
window8.Set_Rect(0,0,240,320);
window8.add_button(&Button8_1);
Button8_1.rect.Set_Rect(90,100,100,100);
Button8_1.text.Set_Text((char *)"ceshi");
Button8_1.Set_Event(&Button8_1_Event);
window0.Refresh();
}
