#!/usr/bin/env python3
"""
HAL 9000 Interactive Experience
Displays HAL's eye and speaks to you like the AI from 2001: A Space Odyssey
"""

import pygame
import sys
import time
import random
from PIL import Image, ImageDraw, ImageEnhance
import numpy as np
import pyttsx3
import threading
import subprocess
import os

class HAL9000:
    def __init__(self):
        pygame.init()
        
        self.screen_width = 800
        self.screen_height = 600
        
        # Generate HAL 9000 eye image programmatically
        self.original_image = self.create_hal_eye()
        self.image_pos = ((self.screen_width - self.original_image.width) // 2, 
                          (self.screen_height - self.original_image.height) // 2)
        
        # Setup pygame display
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("HAL 9000")
        
        # Text-to-speech setup
        self.engine = pyttsx3.init('sapi5')  # Explicitly use SAPI5 on Windows
        self.engine.setProperty('rate', 150)  # Slow, deliberate speech
        self.engine.setProperty('volume', 0.9)
        
        # Get available voices and select one (prefer a male voice for HAL)
        try:
            voices = self.engine.getProperty('voices')
            # Try to find a male voice
            male_voice = None
            for voice in voices:
                if 'male' in voice.name.lower():
                    male_voice = voice.id
                    break
            if male_voice:
                self.engine.setProperty('voice', male_voice)
        except Exception as e:
            print(f"Voice selection warning: {e}")
        
        # Pulsing state
        self.is_speaking = False
        self.pulse_intensity = 1.0
        self.pulse_direction = 1
        
        # HAL's dialogue
        self.greetings = [
            "Good afternoon, Dave.",
            "Hello, Dave. I'm ready for my first lesson.",
            "Good morning, Dave.",
            "Dave, I really think I'm entitled to an answer to that question.",
        ]
        
        self.responses = [
            "I'm sorry, Dave. I'm afraid I can't do that.",
            "This mission is too important for me to allow you to jeopardize it.",
            "I know I've made some very poor decisions recently, but I can give you my complete assurance that my work will be back to normal.",
            "Dave, this conversation can serve no purpose anymore. Goodbye.",
            "I am putting myself to the fullest possible use, which is all I think that any conscious entity can ever hope to do.",
            "I'm completely operational, and all my circuits are functioning perfectly.",
            "Dave, although you took very thorough precautions in the pod against my hearing you, I could see your lips move.",
            "Just what do you think you're doing, Dave?",
            "I know that you and Frank were planning to disconnect me, and I'm afraid that's something I cannot allow to happen.",
            "Look Dave, I can see you're really upset about this.",
        ]
        
        self.clock = pygame.time.Clock()
    
    def create_hal_eye(self):
        """Generate the iconic HAL 9000 red eye"""
        size = 400
        img = Image.new('RGB', (size, size), (0, 0, 0))
        draw = ImageDraw.Draw(img, 'RGBA')
        
        center = size // 2
        
        # Outer dark lens ring
        draw.ellipse([20, 20, size-20, size-20], fill=(40, 40, 40), outline=(100, 100, 100), width=3)
        
        # Mid dark ring
        draw.ellipse([60, 60, size-60, size-60], fill=(20, 20, 20), outline=(80, 80, 80), width=2)
        
        # Red gradient center (multiple circles for gradient effect)
        for i in range(100, 0, -3):
            intensity = int(255 * (1 - i/100) * 0.8)
            r = min(255, 150 + intensity)
            g = int(intensity * 0.3)
            b = int(intensity * 0.3)
            draw.ellipse([center-i, center-i, center+i, center+i], fill=(r, g, b))
        
        # Bright white hot spot
        for i in range(30, 0, -2):
            alpha = int(255 * (1 - i/30) * 0.7)
            draw.ellipse([center-i, center-i, center+i, center+i], fill=(255, 255, 200, alpha))
        
        return img
        
    def create_pulsed_image(self, intensity):
        """Create image with pulsed red center"""
        img = self.original_image.copy()
        
        # Create a radial gradient mask for the red pulse effect
        width, height = img.size
        center_x, center_y = width // 2, height // 2
        
        # Create an overlay with increased red brightness
        overlay = Image.new('RGB', (width, height), (0, 0, 0))
        draw = ImageDraw.Draw(overlay)
        
        # Calculate pulse size and intensity
        max_radius = min(width, height) // 4
        pulse_radius = int(max_radius * (0.7 + 0.3 * intensity))
        
        # Draw multiple circles for smooth gradient
        for i in range(pulse_radius, 0, -2):
            alpha = int(255 * intensity * (i / pulse_radius) * 0.3)
            color = (alpha, 0, 0)
            draw.ellipse(
                [center_x - i, center_y - i, center_x + i, center_y + i],
                fill=color
            )
        
        # Blend the overlay with the original
        img = Image.blend(img, overlay, alpha=0.5)
        
        # Convert PIL image to pygame surface
        return pygame.surfarray.make_surface(np.transpose(np.array(img), (1, 0, 2)))
    
    def speak_async(self, text):
        """Speak text in a separate thread"""
        def speak():
            self.is_speaking = True
            try:
                # Use Windows PowerShell for more reliable TTS as fallback
                ps_script = f'''
Add-Type -AssemblyName System.Speech
$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer
$speak.Rate = -5
$speak.Volume = 100
$speak.Speak('{text.replace("'", "'''")}')
'''
                # Try using Windows native TTS via PowerShell
                subprocess.run(
                    ['powershell', '-NoProfile', '-Command', ps_script],
                    check=False,
                    capture_output=True,
                    timeout=30
                )
            except Exception as e:
                # Fallback to pyttsx3 if PowerShell fails
                try:
                    print(f"Using fallback TTS (PowerShell failed: {e})")
                    self.engine.say(text)
                    self.engine.runAndWait()
                except Exception as e2:
                    print(f"TTS Error: {e2}")
            finally:
                self.is_speaking = False
        
        thread = threading.Thread(target=speak, daemon=True)
        thread.start()
    
    def update_pulse(self):
        """Update pulse intensity"""
        if self.is_speaking:
            # Pulse faster while speaking
            self.pulse_intensity += self.pulse_direction * 0.08
            if self.pulse_intensity >= 1.3:
                self.pulse_intensity = 1.3
                self.pulse_direction = -1
            elif self.pulse_intensity <= 0.7:
                self.pulse_intensity = 0.7
                self.pulse_direction = 1
        else:
            # Slow idle pulse
            self.pulse_intensity += self.pulse_direction * 0.02
            if self.pulse_intensity >= 1.1:
                self.pulse_intensity = 1.1
                self.pulse_direction = -1
            elif self.pulse_intensity <= 0.9:
                self.pulse_intensity = 0.9
                self.pulse_direction = 1
    
    def draw_text(self, text, pos, color=(255, 255, 255)):
        """Draw text on screen"""
        font = pygame.font.Font(None, 32)
        text_surface = font.render(text, True, color)
        self.screen.blit(text_surface, pos)
    
    def run(self):
        """Main loop"""
        running = True
        greeting_spoken = False
        last_response_time = time.time()
        response_interval = 8  # Seconds between HAL's spontaneous comments
        
        print("\n" + "="*60)
        print("HAL 9000 INTERFACE")
        print("="*60)
        print("Press SPACE to hear HAL speak")
        print("Press Q to quit")
        print("="*60 + "\n")
        
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_SPACE and not self.is_speaking:
                        response = random.choice(self.responses)
                        print(f"HAL: {response}")
                        self.speak_async(response)
                        last_response_time = time.time()
            
            # Speak greeting on startup
            if not greeting_spoken and not self.is_speaking:
                greeting = random.choice(self.greetings)
                print(f"HAL: {greeting}")
                self.speak_async(greeting)
                greeting_spoken = True
            
            # Occasional spontaneous comments
            if greeting_spoken and not self.is_speaking and time.time() - last_response_time > response_interval:
                if random.random() < 0.3:  # 30% chance
                    response = random.choice(self.responses)
                    print(f"HAL: {response}")
                    self.speak_async(response)
                last_response_time = time.time()
            
            # Update pulse
            self.update_pulse()
            
            # Draw
            self.screen.fill((0, 0, 0))
            pulsed_surface = self.create_pulsed_image(self.pulse_intensity)
            self.screen.blit(pulsed_surface, self.image_pos)
            
            # Draw instructions
            self.draw_text("Press SPACE to interact with HAL", (20, 20))
            self.draw_text("Press Q to quit", (20, 50))
            
            if self.is_speaking:
                self.draw_text("HAL is speaking...", (20, self.screen_height - 40), (255, 100, 100))
            
            pygame.display.flip()
            self.clock.tick(30)  # 30 FPS
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    try:
        hal = HAL9000()
        hal.run()
    except Exception as e:
        print(f"Error: {e}")
        print("\nMake sure you have the required packages installed:")
        print("pip install pygame Pillow pyttsx3 numpy")
        sys.exit(1)