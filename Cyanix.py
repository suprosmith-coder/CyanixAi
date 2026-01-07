from kivy.lang import Builder
from kivy.app import App
from kivy.uix.imae import Image
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.slider import Slider
from kivy.uix.switch import Switch
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.animation import Animation
from kivy.graphics.texture import Texture
from kivy.properties import StringProperty, NumericProperty, BooleanProperty, ObjectProperty
import requests
import threading
import re
import os
import base64
from datetime import datetime
from PIL import Image as PILImage
import io
import shutil

# Android TTS, Connectivity, Intent, PackageManager
ANDROID_PLATFORM = False
try:
    from jnius import autoclass
    PythonActivity = autoclass('org.kivy.android.PythonActivity')
    Activity = PythonActivity.mActivity
    TTS = autoclass('android.speech.tts.TextToSpeech')
    Locale = autoclass('java.util.Locale')
    ConnectivityManager = autoclass('android.net.ConnectivityManager')
    Context = autoclass('android.content.Context')
    Intent = autoclass('android.content.Intent')
    PackageManager = autoclass('android.content.pm.PackageManager')
    ANDROID_PLATFORM = True
except ImportError:
    pass

Window.clearcolor = (0.95, 0.95, 0.97, 1)

EMBLEM = "cyanix_emblem.png" 
PERSONALITY_FILE = "Personality.txt"

# Modern, clean mobile app UI
KV = '''
#:import FadeTransition kivy.uix.screenmanager.FadeTransition
#:import get_color_from_hex kivy.utils.get_color_from_hex

<MessageBubble@BoxLayout>:
    message_text: ""
    is_user: False
    size_hint_y: None
    height: message_label.texture_size[1] + dp(24)
    padding: 0
    spacing: 0
    
    Widget:
        size_hint_x: 0.15 if root.is_user else None
        width: 0 if not root.is_user else dp(60)
    
    BoxLayout:
        size_hint_x: None
        width: min(dp(280), message_label.texture_size[0] + dp(32))
        padding: dp(16), dp(12)
        canvas.before:
            Color:
                rgba: get_color_from_hex('#007AFF') if root.is_user else get_color_from_hex('#E9E9EB')
            RoundedRectangle:
                pos: self.pos
                size: self.size
                radius: [dp(18), dp(18), dp(4) if root.is_user else dp(18), dp(18) if root.is_user else dp(4)]
        
        Label:
            id: message_label
            text: root.message_text
            color: (1, 1, 1, 1) if root.is_user else (0.1, 0.1, 0.1, 1)
            font_size: '15sp'
            size_hint: None, None
            size: self.texture_size
            text_size: dp(248), None
            markup: True
    
    Widget:
        size_hint_x: 0.15 if not root.is_user else None
        width: 0 if root.is_user else dp(60)

<TopBar@BoxLayout>:
    size_hint_y: None
    height: dp(56)
    padding: dp(16), dp(8)
    spacing: dp(12)
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        Rectangle:
            pos: self.pos
            size: self.size
        Color:
            rgba: 0.9, 0.9, 0.9, 0.3
        Rectangle:
            pos: self.x, self.y
            size: self.width, dp(1)

<ActionButton@Button>:
    size_hint_y: None
    height: dp(44)
    background_normal: ''
    background_color: 0, 0, 0, 0
    font_size: '15sp'
    color: get_color_from_hex('#007AFF')
    canvas.before:
        Color:
            rgba: get_color_from_hex('#F2F2F7')
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(10)]

<SettingsCard@BoxLayout>:
    size_hint_y: None
    height: dp(56)
    padding: dp(16), dp(12)
    spacing: dp(12)
    canvas.before:
        Color:
            rgba: 1, 1, 1, 1
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [dp(12)]

# --- LOGIN SCREEN ---
<LoginScreen>:
    name: "login"
    FloatLayout:
        canvas.before:
            Color:
                rgba: get_color_from_hex('#F2F2F7')
            Rectangle:
                pos: self.pos
                size: self.size

        # Status bar background
        Widget:
            size_hint: 1, None
            height: dp(40)
            pos_hint: {'top': 1}
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size

        BoxLayout:
            orientation: 'vertical'
            size_hint: 0.85, None
            height: dp(420)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            spacing: dp(24)
            padding: dp(20)

            Widget:
                size_hint_y: 0.3

            # App Icon
            FloatLayout:
                size_hint_y: None
                height: dp(100)
                
                Widget:
                    size_hint: None, None
                    size: dp(100), dp(100)
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    canvas.before:
                        Color:
                            rgba: get_color_from_hex('#007AFF')
                        RoundedRectangle:
                            pos: self.pos
                            size: self.size
                            radius: [dp(22)]
                    
                    Image:
                        source: app.emblem_image
                        size_hint: None, None
                        size: dp(60), dp(60)
                        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                        allow_stretch: True
                        keep_ratio: True

            Label:
                text: "Cyanix AI"
                font_size: '32sp'
                color: 0.1, 0.1, 0.1, 1
                bold: True
                size_hint_y: None
                height: dp(40)

            Label:
                text: "Your intelligent assistant"
                font_size: '16sp'
                color: 0.4, 0.4, 0.4, 1
                size_hint_y: None
                height: dp(24)

            Widget:
                size_hint_y: None
                height: dp(32)

            # Modern text input
            BoxLayout:
                size_hint_y: None
                height: dp(50)
                padding: 0
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(12)]
                    Color:
                        rgba: 0.85, 0.85, 0.85, 1
                    Line:
                        rounded_rectangle: self.x, self.y, self.width, self.height, dp(12)
                        width: dp(1)
                
                TextInput:
                    id: username_input
                    hint_text: "Enter your name"
                    multiline: False
                    background_color: 0, 0, 0, 0
                    foreground_color: 0.1, 0.1, 0.1, 1
                    cursor_color: get_color_from_hex('#007AFF')
                    padding: dp(16), dp(15)
                    font_size: '16sp'
                    hint_text_color: 0.6, 0.6, 0.6, 1
                    on_text_validate: app.authenticate_user(self.text)

            Button:
                text: "Continue"
                size_hint_y: None
                height: dp(50)
                background_normal: ''
                background_color: 0, 0, 0, 0
                font_size: '17sp'
                bold: True
                color: 1, 1, 1, 1
                on_release: app.authenticate_user(username_input.text)
                canvas.before:
                    Color:
                        rgba: get_color_from_hex('#007AFF')
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(12)]

            Widget:
                size_hint_y: 1

# --- CHAT SCREEN ---
<ChatScreen>:
    name: "chat"
    BoxLayout:
        orientation: 'vertical'
        canvas.before:
            Color:
                rgba: get_color_from_hex('#F2F2F7')
            Rectangle:
                pos: self.pos
                size: self.size

        # Top Navigation Bar
        TopBar:
            Button:
                text: "☰"
                size_hint_x: None
                width: dp(40)
                background_normal: ''
                background_color: 0, 0, 0, 0
                font_size: '24sp'
                color: 0.1, 0.1, 0.1, 1
                on_release: app.toggle_menu()
            
            Label:
                text: "Cyanix AI"
                font_size: '18sp'
                bold: True
                color: 0.1, 0.1, 0.1, 1
                size_hint_x: 1
            
            Widget:
                size_hint: None, None
                size: dp(12), dp(12)
                pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                canvas.before:
                    Color:
                        rgba: get_color_from_hex('#34C759') if app.is_online() else get_color_from_hex('#FF3B30')
                    Ellipse:
                        pos: self.pos
                        size: self.size

        # Chat Area
        ScrollView:
            id: chat_scroll
            do_scroll_x: False
            scroll_type: ['bars']
            bar_width: dp(4)
            bar_color: 0.7, 0.7, 0.7, 0.5
            
            BoxLayout:
                id: chat_history
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                spacing: dp(8)
                padding: dp(16), dp(12)

        # Input Area
        BoxLayout:
            size_hint_y: None
            height: max(dp(56), input_field.minimum_height + dp(16))
            padding: dp(12), dp(8)
            spacing: dp(8)
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1
                Rectangle:
                    pos: self.pos
                    size: self.size
                Color:
                    rgba: 0.9, 0.9, 0.9, 0.5
                Rectangle:
                    pos: self.x, self.y + self.height - dp(1)
                    size: self.width, dp(1)
            
            BoxLayout:
                size_hint_x: 1
                padding: dp(12), dp(8)
                canvas.before:
                    Color:
                        rgba: get_color_from_hex('#E9E9EB')
                    RoundedRectangle:
                        pos: self.pos
                        size: self.size
                        radius: [dp(20)]
                
                TextInput:
                    id: input_field
                    hint_text: "Message"
                    hint_text_color: 0.6, 0.6, 0.6, 1
                    multiline: True
                    size_hint_y: None
                    height: max(dp(24), self.minimum_height)
                    background_color: 0, 0, 0, 0
                    foreground_color: 0.1, 0.1, 0.1, 1
                    cursor_color: get_color_from_hex('#007AFF')
                    font_size: '16sp'
                    padding: 0
                    on_text_validate: app.send_message()
            
            Button:
                text: "↑"
                size_hint: None, None
                size: dp(36), dp(36)
                background_normal: ''
                background_color: 0, 0, 0, 0
                font_size: '24sp'
                color: 1, 1, 1, 1
                on_release: app.send_message()
                canvas.before:
                    Color:
                        rgba: get_color_from_hex('#007AFF')
                    Ellipse:
                        pos: self.pos
                        size: self.size

        # Side Menu (hidden by default)
        FloatLayout:
            id: menu_overlay
            opacity: 0
            disabled: True
            
            # Dark overlay
            Widget:
                canvas.before:
                    Color:
                        rgba: 0, 0, 0, 0.4
                    Rectangle:
                        pos: self.pos
                        size: self.size
                on_touch_down: if self.collide_point(*args[1].pos): app.toggle_menu()
            
            # Menu panel
            BoxLayout:
                id: menu_panel
                orientation: 'vertical'
                size_hint: 0.75, 1
                pos_hint: {'x': -0.75, 'y': 0}
                padding: dp(20), dp(60), dp(20), dp(20)
                spacing: dp(20)
                canvas.before:
                    Color:
                        rgba: 1, 1, 1, 1
                    Rectangle:
                        pos: self.pos
                        size: self.size
                
                # User Profile Section
                BoxLayout:
                    size_hint_y: None
                    height: dp(80)
                    spacing: dp(12)
                    
                    Widget:
                        size_hint: None, None
                        size: dp(60), dp(60)
                        canvas.before:
                            Color:
                                rgba: get_color_from_hex('#007AFF')
                            Ellipse:
                                pos: self.pos
                                size: self.size
                        
                        Label:
                            text: app.current_username[0].upper() if app.current_username else "?"
                            font_size: '28sp'
                            bold: True
                            color: 1, 1, 1, 1
                            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    
                    BoxLayout:
                        orientation: 'vertical'
                        spacing: dp(2)
                        
                        Label:
                            text: app.current_username
                            font_size: '18sp'
                            bold: True
                            color: 0.1, 0.1, 0.1, 1
                            halign: 'left'
                            valign: 'bottom'
                            text_size: self.size
                        
                        Label:
                            text: "Active User"
                            font_size: '14sp'
                            color: 0.5, 0.5, 0.5, 1
                            halign: 'left'
                            valign: 'top'
                            text_size: self.size

                Widget:
                    size_hint_y: None
                    height: dp(1)
                    canvas.before:
                        Color:
                            rgba: 0.9, 0.9, 0.9, 1
                        Rectangle:
                            pos: self.pos
                            size: self.size

                ScrollView:
                    do_scroll_x: False
                    
                    BoxLayout:
                        orientation: 'vertical'
                        size_hint_y: None
                        height: self.minimum_height
                        spacing: dp(8)
                        
                        Label:
                            text: "AI MODE"
                            font_size: '13sp'
                            bold: True
                            color: 0.5, 0.5, 0.5, 1
                            size_hint_y: None
                            height: dp(32)
                            halign: 'left'
                            valign: 'bottom'
                            text_size: self.size
                        
                        ActionButton:
                            text: "⚡ Nix - Quick Responses"
                            on_release: app.set_ai_mode('nix')
                        
                        ActionButton:
                            text: "🧠 Nova - Deep Thinking"
                            on_release: app.set_ai_mode('blub')
                        
                        ActionButton:
                            text: "🤖 Cyanix - Balanced"
                            on_release: app.set_ai_mode('default')
                        
                        Widget:
                            size_hint_y: None
                            height: dp(16)
                        
                        Label:
                            text: "SETTINGS"
                            font_size: '13sp'
                            bold: True
                            color: 0.5, 0.5, 0.5, 1
                            size_hint_y: None
                            height: dp(32)
                            halign: 'left'
                            valign: 'bottom'
                            text_size: self.size
                        
                        SettingsCard:
                            Label:
                                text: "Voice Speed"
                                color: 0.1, 0.1, 0.1, 1
                                font_size: '15sp'
                                size_hint_x: 0.4
                            
                            Slider:
                                id: voice_speed_slider
                                min: 0.5
                                max: 1.5
                                value: 0.9
                                size_hint_x: 0.6
                                on_value: app.update_voice_speed(self.value)
                        
                        SettingsCard:
                            Label:
                                text: "Auto-Speak"
                                color: 0.1, 0.1, 0.1, 1
                                font_size: '15sp'
                            
                            Widget:
                                size_hint_x: 1
                            
                            Switch:
                                id: auto_speak_switch
                                active: True
                                size_hint_x: None
                                width: dp(51)
                                on_active: app.toggle_auto_speak(self.active)
                        
                        Widget:
                            size_hint_y: None
                            height: dp(16)
                        
                        Label:
                            text: "ACTIONS"
                            font_size: '13sp'
                            bold: True
                            color: 0.5, 0.5, 0.5, 1
                            size_hint_y: None
                            height: dp(32)
                            halign: 'left'
                            valign: 'bottom'
                            text_size: self.size
                        
                        ActionButton:
                            text: "🧹 Clear Chat"
                            on_release: app.clear_chat()
                        
                        ActionButton:
                            text: "💾 Export Chat"
                            on_release: app.export_chat()
                        
                        ActionButton:
                            text: "📂 Load Memory"
                            on_release: app.load_memory()
                        
                        ActionButton:
                            text: "🗑 Clear Memory"
                            on_release: app.clear_memory()
                        
                        Widget:
                            size_hint_y: None
                            height: dp(16)
                        
                        ActionButton:
                            text: "🚪 Logout"
                            color: get_color_from_hex('#FF3B30')
                            on_release: app.logout()

ScreenManager:
    transition: FadeTransition()
    LoginScreen:
    ChatScreen:
'''

class LoginScreen(Screen):
    pass

class ChatScreen(Screen):
    pass

class CyanixApp(App):
    emblem_image = StringProperty(EMBLEM)
    status_text = StringProperty("• ONLINE")
    status_expanded = BooleanProperty(False)
    system_info_text = StringProperty("")
    auto_speak_enabled = BooleanProperty(True)
    menu_open = BooleanProperty(False)
    
    current_username = StringProperty("Unknown")
    current_memory_file = StringProperty("")
    current_mode = StringProperty("default")
    
    # Using free API keys (you should replace these with your own)
    GROQ_KEYS = [
        "Grok_key",
    ]
    
    OPENAI_KEYS = ["sk-proj-your-key-here"]
    GEMINI_KEYS = ["AIzaSyC0UkFEAko1jmZ-sLxHvsVZii55LRaC4aI"]
    XAI_KEYS = ["xai-kfzssxeOTu5GLx3nXgj4POdYkU3yPVdcep2FbLcHzPnr2h36gMOkZxK2Oy8coWmm2eod7THiITavu41m"]
    
    current_groq_index = NumericProperty(0)
    current_openai_index = NumericProperty(0)
    current_gemini_index = NumericProperty(0)
    current_xai_index = NumericProperty(0)

    def build(self):
        if not os.path.exists(EMBLEM):
            # Create a simple emblem if it doesn't exist
            try:
                from kivy.core.image import Image as CoreImage
                from kivy.graphics import Color, Ellipse
                texture = Texture.create(size=(100, 100), colorfmt='rgba')
                texture.blit_buffer(b'\xff\x7f\x00\xff' * 10000, colorfmt='rgba', bufferfmt='ubyte')
                texture.save(EMBLEM)
            except:
                print(f"WARNING: {EMBLEM} not found. Using default.")
                self.emblem_image = ""

        self.load_personality()
        
        if ANDROID_PLATFORM:
            try:
                self.tts = TTS(Activity, None)
                self.tts.setLanguage(Locale.US)
                self.tts.setSpeechRate(0.9)
                self.cm = Activity.getSystemService(Context.CONNECTIVITY_SERVICE)
                self.pm = Activity.getPackageManager()
                self.intent_filter = autoclass('android.content.IntentFilter')(autoclass('android.content.Intent').ACTION_BATTERY_CHANGED)
                Window.softinput_mode = 'pan'
            except Exception as e:
                print(f"Android init error: {e}")
        
        Clock.schedule_interval(self.update_status, 5)
        self.update_system_info()
        
        return Builder.load_string(KV)

    def get_chat_screen_ids(self):
        """Helper to get IDs from the chat screen"""
        return self.root.get_screen('chat').ids

    def toggle_menu(self):
        """Open/close side menu with animation"""
        chat_ids = self.get_chat_screen_ids()
        if not chat_ids:
            return
            
        menu_overlay = chat_ids.menu_overlay
        menu_panel = chat_ids.menu_panel
        
        if self.menu_open:
            # Close menu
            anim_panel = Animation(pos_hint={'x': -0.75, 'y': 0}, duration=0.3)
            anim_overlay = Animation(opacity=0, duration=0.3)
            anim_panel.start(menu_panel)
            anim_overlay.start(menu_overlay)
            anim_overlay.bind(on_complete=lambda *args: setattr(menu_overlay, 'disabled', True))
            self.menu_open = False
        else:
            # Open menu
            menu_overlay.disabled = False
            anim_panel = Animation(pos_hint={'x': 0, 'y': 0}, duration=0.3)
            anim_overlay = Animation(opacity=1, duration=0.3)
            anim_panel.start(menu_panel)
            anim_overlay.start(menu_overlay)
            self.menu_open = True

    def authenticate_user(self, username):
        """Handle user login and memory file creation/loading"""
        username = username.strip()
        if not username:
            return

        self.current_username = username
        safe_username = "".join(x for x in username if x.isalnum())
        self.current_memory_file = f"Memory_{safe_username}.txt"
        
        is_new_user = False
        
        if not os.path.exists(self.current_memory_file):
            is_new_user = True
            try:
                with open(self.current_memory_file, "w", encoding="utf-8") as f:
                    f.write(f"System: User {username} registered at {datetime.now()}\n\n")
            except Exception as e:
                print(f"Error creating user memory: {e}")

        self.root.current = "chat"
        self.load_conversation_history()
        Clock.schedule_once(lambda dt: self.greet_user(username, is_new_user), 1)

    def greet_user(self, username, is_new_user):
        """Send welcome message based on user status"""
        if is_new_user:
            msg = f"Hello {username}! I'm Cyanix, your AI assistant. How can I help you today?"
        else:
            msg = f"Welcome back, {username}!"
            
        self.add_message_bubble(msg, is_user=False)
        if self.auto_speak_enabled and ANDROID_PLATFORM:
            self.speak(msg)

    def logout(self):
        """Logout and return to login screen"""
        self.root.current = "login"
        self.current_username = "Unknown"
        self.current_memory_file = ""
        self.get_chat_screen_ids().chat_history.clear_widgets()
        if self.menu_open:
            self.toggle_menu()

    def clear_memory(self):
        """Clear memory file for current user"""
        try:
            if os.path.exists(self.current_memory_file):
                os.remove(self.current_memory_file)
                with open(self.current_memory_file, "w", encoding="utf-8") as f:
                    f.write("")
            
            if self.auto_speak_enabled and ANDROID_PLATFORM:
                self.speak("Memory cleared")
            self.add_message_bubble("Memory cleared successfully", is_user=False)
        except Exception as e:
            self.add_message_bubble(f"Error: {str(e)}", is_user=False)

    def load_memory(self):
        """Load and display conversation from memory"""
        try:
            chat_history = self.get_chat_screen_ids().chat_history
            if os.path.exists(self.current_memory_file):
                with open(self.current_memory_file, "r", encoding="utf-8") as f:
                    content = f.read()
                if content.strip():
                    chat_history.clear_widgets()
                    lines = content.strip().split("\n\n")
                    for line in lines:
                        if line.strip():
                            if line.startswith("You:"):
                                msg = line.replace("You:", "").strip()
                                self.add_message_bubble(msg, is_user=True)
                            elif line.startswith("Cyanix AI:"):
                                msg = line.replace("Cyanix AI:", "").strip()
                                self.add_message_bubble(msg, is_user=False)
                else:
                    self.add_message_bubble("Memory is empty", is_user=False)
        except Exception as e:
            self.add_message_bubble(f"Error: {str(e)}", is_user=False)

    def load_conversation_history(self):
        """Automatically load conversation history on startup"""
        if not self.current_memory_file:
            return
            
        try:
            if os.path.exists(self.current_memory_file):
                with open(self.current_memory_file, "r", encoding="utf-8") as f:
                    content = f.read()
                if content.strip():
                    lines = content.strip().split("\n\n")
                    for line in lines[-20:]:
                        if line.strip():
                            if line.startswith("You:"):
                                msg = line.replace("You:", "").strip()
                                self.add_message_bubble(msg, is_user=True)
                            elif line.startswith("Cyanix AI:"):
                                msg = line.replace("Cyanix AI:", "").strip()
                                self.add_message_bubble(msg, is_user=False)
        except Exception as e:
            print(f"Error loading history: {e}")

    def save_to_memory(self, sender, text):
        """Save message to specific user memory file"""
        if not self.current_memory_file:
            return
        try:
            with open(self.current_memory_file, "a", encoding="utf-8") as f:
                f.write(f"{sender}: {text}\n\n")
        except Exception as e:
            print(f"Error saving to memory: {e}")

    def update_voice_speed(self, value):
        if ANDROID_PLATFORM and hasattr(self, 'tts'):
            self.tts.setSpeechRate(value)

    def toggle_auto_speak(self, active):
        self.auto_speak_enabled = active

    def clear_chat(self):
        self.get_chat_screen_ids().chat_history.clear_widgets()
        if self.menu_open:
            self.toggle_menu()

    def export_chat(self):
        """Export chat history to file"""
        try:
            if os.path.exists(self.current_memory_file):
                export_name = f"Chat_Export_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                shutil.copy(self.current_memory_file, export_name)
                self.add_message_bubble(f"Chat exported to {export_name}", is_user=False)
                if self.auto_speak_enabled and ANDROID_PLATFORM and hasattr(self, 'tts'):
                    self.speak("Chat exported successfully")
        except Exception as e:
            self.add_message_bubble(f"Export error: {str(e)}", is_user=False)
        
        if self.menu_open:
            self.toggle_menu()

    def add_message_bubble(self, text, is_user=False):
        """Add a message bubble to chat history using the KV class"""
        from kivy.factory import Factory
        
        # Create the message bubble using the KV class
        bubble = Factory.MessageBubble()
        bubble.message_text = text
        bubble.is_user = is_user
        
        chat_ids = self.get_chat_screen_ids()
        if chat_ids:
            chat_ids.chat_history.add_widget(bubble)
            Clock.schedule_once(lambda dt: setattr(chat_ids.chat_scroll, 'scroll_y', 0), 0.1)

    def update_status(self, dt):
        # Status updates handled in UI
        pass

    def update_system_info(self):
        if ANDROID_PLATFORM:
            try:
                battery_status = Activity.registerReceiver(None, self.intent_filter)
                level = battery_status.getIntExtra("level", -1)
                scale = battery_status.getIntExtra("scale", -1)
                battery_pct = int(level / scale * 100) if scale > 0 else 0
            except:
                battery_pct = "N/A"
        else:
            battery_pct = 100

        now = datetime.now()
        time_str = now.strftime("%H:%M")
        date_str = now.strftime("%b %d, %Y")

        self.system_info_text = f"Time: {time_str}\nDate: {date_str}\nBattery: {battery_pct}%"
        Clock.schedule_once(lambda dt: self.update_system_info(), 60)

    def send_message(self):
        chat_ids = self.get_chat_screen_ids()
        if not chat_ids:
            return
            
        user_input = chat_ids.input_field.text.strip()
        if not user_input:
            return

        lower_input = user_input.lower()
        
        if lower_input in ["logout", "exit", "log out"]:
            self.logout()
            chat_ids.input_field.text = ""
            return

        if lower_input.startswith("open ") and ANDROID_PLATFORM:
            app = lower_input[5:].strip()
            if self.launch_app(app):
                chat_ids.input_field.text = ""
                return

        self.add_message_bubble(user_input, is_user=True)
        self.save_to_memory("You", user_input)
        chat_ids.input_field.text = ""

        threading.Thread(target=self.process_query, args=(user_input,), daemon=True).start()

    def process_query(self, user_input):
        system_prompt = f"You are Cyanix AI. You are speaking to {self.current_username}."
        if hasattr(self, 'personality'):
            system_prompt += f"\n\nPersonality:\n{self.personality}"

        if self.current_mode == "nix":
            system_prompt += "\n\nYou are in 'Nix' mode: Respond quickly, concisely, and directly. Avoid long explanations unless asked."
        elif self.current_mode == "blub":
            system_prompt += "\n\nYou are in 'Nova' mode: Think deeply, provide detailed reasoning, explore possibilities, and give thorough answers."

        if "generate image" in user_input.lower() or "create image" in user_input.lower() or "make image" in user_input.lower():
            self.set_ai_mode('blub')

        context_messages = [{"role": "system", "content": system_prompt}]
        
        try:
            if os.path.exists(self.current_memory_file):
                with open(self.current_memory_file, "r", encoding="utf-8") as f:
                    memory_content = f.read()
                    lines = memory_content.strip().split("\n\n")
                    recent_lines = lines[-10:] if self.current_mode == "nix" else lines[-20:]
                    for line in recent_lines:
                        if line.startswith("You:"):
                            context_messages.append({"role": "user", "content": line.replace("You:", "").strip()})
                        elif line.startswith("Cyanix AI:"):
                            context_messages.append({"role": "assistant", "content": line.replace("Cyanix AI:", "").strip()})
        except Exception:
            pass
        
        context_messages.append({"role": "user", "content": user_input})

        if not self.is_online():
            ai_text = "Internet connection required for AI responses."
            Clock.schedule_once(lambda dt: self.deliver_response(ai_text))
            return

        is_complex = len(user_input) > 100 or any(word in user_input.lower() for word in ["explain", "analyze", "reason", "deep", "code", "math"])
        is_multimodal = any(word in user_input.lower() for word in ["image", "picture", "visual", "describe photo"])

        if self.current_mode == "nix" or not is_complex:
            preferred_provider = "groq"
        elif self.current_mode == "blub" or is_complex:
            preferred_provider = "xai"
        else:
            preferred_provider = "google" if is_multimodal else "openai"

        temperature = 0.5 if self.current_mode == "nix" else 0.9 if self.current_mode == "blub" else 0.7
        max_tokens = 512 if self.current_mode == "nix" else 2048 if self.current_mode == "blub" else 1024

        fallback_providers = ["openai", "xai", "google", "groq"]
        providers_to_try = [preferred_provider] + [p for p in fallback_providers if p != preferred_provider]

        ai_text = "All API attempts failed. Check keys and connection."
        for prov in providers_to_try:
            model = self.get_model_for_provider(prov, self.current_mode, is_multimodal)
            ai_text = self._make_api_call(prov, model, context_messages, temperature, max_tokens)
            if "Error" not in ai_text and "failed" not in ai_text:
                break
            else:
                print(f"Fallback from {prov}: {ai_text}")

        Clock.schedule_once(lambda dt: self.deliver_response(ai_text))

    def get_model_for_provider(self, provider, mode, is_multimodal):
        if provider == "groq":
            if mode == "blub" or is_multimodal:
                return "llama-3.3-70b-versatile"
            else:
                return "llama-3.1-8b-instant"
        elif provider == "openai":
            return "gpt-4o"
        elif provider == "xai":
            return "grok-beta"
        elif provider == "google":
            if is_multimodal:
                return "gemini-pro-vision"
            else:
                return "gemini-pro"
        return "unknown-model"

    def _make_api_call(self, provider, model, messages, temperature, max_tokens):
        attempts = 0
        max_attempts = 2
        
        while attempts < max_attempts:
            try:
                if provider == "groq":
                    if not self.GROQ_KEYS:
                        return "No Groq API keys configured"
                    api_key = self.GROQ_KEYS[self.current_groq_index % len(self.GROQ_KEYS)]
                    url = "https://api.groq.com/openai/v1/chat/completions"
                    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
                    self.current_groq_index += 1
                    
                elif provider == "openai":
                    if not self.OPENAI_KEYS:
                        return "No OpenAI API keys configured"
                    api_key = self.OPENAI_KEYS[self.current_openai_index % len(self.OPENAI_KEYS)]
                    url = "https://api.openai.com/v1/chat/completions"
                    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
                    self.current_openai_index += 1
                    
                elif provider == "xai":
                    if not self.XAI_KEYS:
                        return "No xAI API keys configured"
                    api_key = self.XAI_KEYS[self.current_xai_index % len(self.XAI_KEYS)]
                    url = "https://api.x.ai/v1/chat/completions"
                    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
                    self.current_xai_index += 1
                    
                elif provider == "google":
                    if not self.GEMINI_KEYS:
                        return "No Google API keys configured"
                    api_key = self.GEMINI_KEYS[self.current_gemini_index % len(self.GEMINI_KEYS)]
                    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
                    headers = {"Content-Type": "application/json"}
                    self.current_gemini_index += 1
                    
                    contents = []
                    for msg in messages:
                        role = "user" if msg["role"] in ["user", "system"] else "model"
                        contents.append({"role": role, "parts": [{"text": msg["content"]}]})
                    payload = {
                        "contents": contents,
                        "generationConfig": {
                            "temperature": temperature,
                            "maxOutputTokens": max_tokens
                        }
                    }
                    response = requests.post(url, headers=headers, json=payload, timeout=30)
                    response.raise_for_status()
                    result = response.json()
                    return result["candidates"][0]["content"]["parts"][0]["text"].strip()
                    
                else:
                    return "Unknown provider"
                
                if provider != "google":
                    payload = {
                        "model": model,
                        "messages": messages,
                        "temperature": temperature,
                        "max_tokens": max_tokens
                    }
                    response = requests.post(url, headers=headers, json=payload, timeout=30)
                    response.raise_for_status()
                    result = response.json()
                    return result["choices"][0]["message"]["content"].strip()
                    
            except requests.exceptions.RequestException as e:
                if attempts == max_attempts - 1:
                    return f"API Error: {str(e)}"
            except Exception as e:
                if attempts == max_attempts - 1:
                    return f"Error: {str(e)}"
            
            attempts += 1
        
        return "All attempts failed for this provider."

    def deliver_response(self, ai_text):
        formatted = re.sub(r'([.!?])\s*(?=[A-Z])', r'\1\n\n', ai_text).strip()
        self.add_message_bubble(formatted, is_user=False)
        if self.auto_speak_enabled and ANDROID_PLATFORM and hasattr(self, 'tts'):
            self.speak(formatted)
        self.save_to_memory("Cyanix AI", formatted)

    def set_ai_mode(self, mode):
        valid_modes = ["default", "nix", "blub"]
        if mode not in valid_modes:
            return
        self.current_mode = mode
        
        mode_names = {
            "default": "Cyanix",
            "nix": "Nix",
            "blub": "Nova"
        }
        
        self.add_message_bubble(f"AI mode: {mode_names[mode]}", is_user=False)
        if self.auto_speak_enabled and ANDROID_PLATFORM and hasattr(self, 'tts'):
            self.speak(f"Mode switched to {mode_names[mode].lower()}.")
        
        if self.menu_open:
            self.toggle_menu()

    def load_personality(self):
        if os.path.exists(PERSONALITY_FILE):
            try:
                with open(PERSONALITY_FILE, "r", encoding="utf-8") as f:
                    self.personality = f.read().strip()
            except:
                self.personality = ""
        else:
            self.personality = ""

    def is_online(self):
        try:
            requests.get("https://www.google.com", timeout=3)
            return True
        except:
            return False
    
    def launch_app(self, app_name):
        if not ANDROID_PLATFORM: 
            return False
        package_map = {
            "youtube": "com.google.android.youtube",
            "chrome": "com.android.chrome",
            "camera": "com.android.camera2",
            "gallery": "com.android.gallery3d",
            "settings": "com.android.settings",
            "play store": "com.android.vending",
        }
        package = package_map.get(app_name)
        if package:
            try:
                intent = self.pm.getLaunchIntentForPackage(package)
                if intent:
                    Activity.startActivity(intent)
                    if self.auto_speak_enabled:
                        self.speak(f"Opening {app_name}.")
                    return True
            except:
                pass
        return False

    def speak(self, text):
        if not ANDROID_PLATFORM or not hasattr(self, 'tts'):
            return
        clean = re.sub(r'\[.*?\]', '', text)
        self.tts.speak(clean, TTS.QUEUE_FLUSH, None)

if __name__ == '__main__':
    CyanixApp().run()
if __name__ == '__main__':
    CyanixApp().run()