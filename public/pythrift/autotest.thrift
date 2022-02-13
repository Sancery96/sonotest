namespace cpp testframe //variable information/** * The first thing to know about are types. The available types in Thrift are: * *  bool        Boolean, one byte *  byte        Signed byte *  i16         Signed 16-bit integer *  i32         Signed 32-bit integer *  i64         Signed 64-bit integer *  double      64-bit floating point value *  string      String *  binary      Blob (byte array) *  map<t1,t2>  Map from one type to another *  list<t1>    Ordered list of one type *  set<t1>     Set of unique elements of one type * * Did you also notice that Thrift supports C style comments? */service autotest {   //utility api   string get_sw_version(),   string get_machine_type(),   string get_record_file(),         //case api   i32 panel_event(1:i32 type, 2:string func_name, 3:i16 wparam, 4:i64 lparam),   i32 key_event(1:i32 key, 2:string key_str),   i32 param_adjust(1:string func_name, 2:i32 key, 3:i32 which),   i32 TGC_adjust(1:i32 type, 2:string func_name, 3:i32 index, 4:i32 value),   i32 mousebutton_event(1:i32 type, 2:i32 button),   i32 mousemove_to_event(1:i64 x, 2:i64 y),     i32 mousemove_rel_event(1:i64 x, 2:i64 y),    i32 touchscreen_event(1:i32 Tpmsg, 2:i32 wParam, 3:i32 lParam),      i32 force_probe(1:i32 probeId, 2:bool Endforce),    bool enter_exam(1:i32 slotIndex, 2:i32 count),   i32 save_current_screen(1:string casename, 2:i32 linenum),   i32 mouse_press_event(1:i32 button),   i32 mouse_release_event(1:i32 button),   i32 LGC_adjust(1:string func_name, 2:i32 index, 3:i32 value),   i32 touchscreen_measure(1:i32 section, 2:i32 id, 3:i32 side, 4:i32 step),   i32 get_led_status(1:string func_name),   i32 write_log_message(1:i32 state, 2:string log_message),   //widget api   bool     get_widget_is_enable(1:string name),   string   get_checkbox_text(1:string name),   string   get_pushbutton_text(1:string name),   string   get_radiobutton_text(1:string name),   string   get_toolbutton_text(1:string name),   i32      get_tab_widget_count(1:string name),   i32      get_tab_widget_current_index(1:string name),   string   get_tab_widget_current_text(1:string name),   map<string, bool> get_tab_widget_name_list(1:string name),   i32      get_table_widget_row_count(1:string name),   i32      get_table_widget_column_count(1:string name),   string   get_label_text(1:string name),   i32      get_combobox_count(1:string name),   list<string> get_combobox_text_list(1:string name),   string   get_combobox_current_text(1:string name),   i32      get_combobox_current_index(1:string name),   bool     get_checkbox_state(1:string name),   string   get_lineedit_text(1:string name),   i32      get_spinbox_value(1:string name),   double   get_doublespinbox_value(1:string name),   i32      get_widget_width(1:string name),   i32      get_widget_height(1:string name),      i32      set_widget_enable(1:string name, 2:bool enable),   i32      checkbox_click(1:string name),   i32      pushbutton_click(1:string name),   i32      radiobutton_click(1:string name),   i32      toolbutton_click(1:string name),   i32      set_checkbox_text(1:string name, 2:string text),   i32      set_pushbutton_text(1:string name, 2:string text),   i32      set_radiobutton_text(1:string name, 2:string text),   i32      set_toolbutton_text(1:string name, 2:string text),   i32      set_tab_widget_current_index(1:string name, 2:i32 index),   i32      set_tab_widget_current_text(1:string name, 2:string text),   i32      set_table_widget_row_checked(1:string name, 2:bool checked, 3:i32 row),   i32      set_table_widget_row_range_checked(1:string name, 2:bool checked, 3:i32 row_start, 4:i32 row_end),   i32      set_label_text(1:string name, 2:string text),   i32      set_combobox_current_index(1:string name, 2:i32 index),   i32      set_combobox_current_text(1:string name, 2:string text),   i32      set_checkbox_state(1:string name, 2:bool state),   i32      set_lineedit_text(1:string name, 2:string text),   i32      set_spinbox_value(1:string name, 2:i32 value),   i32      spinbox_step_up(1:string name),   i32      spinbox_step_down(1:string name),   i32      set_doublespinbox_value(1:string name, 2:double value),   i32      doublespinbox_step_up(1:string name),   i32      doublespinbox_step_down(1:string name),   i32      mouse_move_to_widget(1:string name),}