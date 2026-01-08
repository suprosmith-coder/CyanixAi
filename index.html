<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cyanix AI</title>
    
    <!-- PWA Configuration -->
    <link rel="manifest" href="/CyanixAi/manifest.json">
    <meta name="theme-color" content="#0d0221">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <link rel="apple-touch-icon" href="/CyanixAi/icons/icon-192x192.png">
    
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        :root {
            --cyan-neon: #00f3ff;
            --cyan-dark: #00a8b5;
            --cyan-bright: #6bffff;
            --purple-deep: #1a0633;
            --purple-dark: #0d0221;
            --neon-glow: 0 0 10px var(--cyan-neon), 0 0 20px var(--cyan-neon), 0 0 30px var(--cyan-neon);
            --ship-glow: 0 0 15px var(--cyan-neon), 0 0 30px var(--cyan-neon), 0 0 45px var(--cyan-neon);
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            background: var(--purple-dark);
            height: 100vh;
            overflow: hidden;
            position: fixed;
            width: 100%;
        }

        /* Milky Way Galaxy Background */
        .galaxy-background {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(ellipse at 20% 20%, rgba(157, 78, 221, 0.3) 0%, transparent 40%),
                radial-gradient(ellipse at 80% 80%, rgba(0, 243, 255, 0.3) 0%, transparent 40%),
                radial-gradient(ellipse at 50% 50%, rgba(45, 27, 105, 0.6) 0%, transparent 70%),
                linear-gradient(135deg, #0d0221 0%, #1a0633 30%, #2d1b69 70%, #0d0221 100%);
            z-index: -1;
            overflow: hidden;
        }

        .galaxy-core {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 300px;
            height: 150px;
            background: radial-gradient(circle, rgba(255, 255, 255, 0.8) 0%, rgba(255, 255, 180, 0.4) 20%, transparent 70%);
            border-radius: 50%;
            filter: blur(40px);
            opacity: 0.7;
            transform: translate(-50%, -50%);
            animation: corePulse 8s infinite alternate;
        }

        @keyframes corePulse {
            0% { opacity: 0.5; transform: translate(-50%, -50%) scale(1); }
            100% { opacity: 0.8; transform: translate(-50%, -50%) scale(1.2); }
        }

        .galaxy-arm {
            position: absolute;
            top: 50%;
            left: 50%;
            width: 800px;
            height: 400px;
            border-radius: 50%;
            border: 1px solid transparent;
            box-shadow: 
                0 0 100px rgba(157, 78, 221, 0.3),
                0 0 200px rgba(157, 78, 221, 0.2),
                0 0 300px rgba(157, 78, 221, 0.1);
            transform: translate(-50%, -50%) rotate(var(--rotation));
            opacity: 0.4;
        }

        .arm-1 { --rotation: 0deg; }
        .arm-2 { --rotation: 120deg; }
        .arm-3 { --rotation: 240deg; }

        .stars {
            position: absolute;
            width: 100%;
            height: 100%;
        }

        .star {
            position: absolute;
            background: white;
            border-radius: 50%;
            animation: twinkle 3s infinite;
        }

        .star.large {
            width: 3px;
            height: 3px;
            box-shadow: 0 0 10px white, 0 0 20px white;
        }

        .star.medium {
            width: 2px;
            height: 2px;
            box-shadow: 0 0 5px white, 0 0 10px white;
        }

        .star.small {
            width: 1px;
            height: 1px;
            box-shadow: 0 0 3px white;
        }

        @keyframes twinkle {
            0%, 100% { opacity: 0.3; transform: scale(1); }
            50% { opacity: 1; transform: scale(1.2); }
        }

        /* Spaceships */
        .spaceship {
            position: absolute;
            z-index: 2;
            filter: drop-shadow(0 0 10px var(--cyan-neon));
        }

        .spaceship.large {
            width: 60px;
            height: 30px;
        }

        .spaceship.medium {
            width: 40px;
            height: 20px;
        }

        .spaceship.small {
            width: 20px;
            height: 10px;
        }

        .spaceship-body {
            position: absolute;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, 
                rgba(0, 243, 255, 0.1) 0%,
                rgba(0, 243, 255, 0.8) 50%,
                rgba(0, 243, 255, 0.1) 100%);
            clip-path: polygon(0% 0%, 80% 0%, 100% 50%, 80% 100%, 0% 100%);
            border-radius: 4px;
        }

        .spaceship-wings {
            position: absolute;
            width: 120%;
            height: 40%;
            top: 30%;
            left: -10%;
            background: linear-gradient(90deg, 
                transparent 0%,
                rgba(0, 243, 255, 0.4) 30%,
                rgba(0, 243, 255, 0.8) 50%,
                rgba(0, 243, 255, 0.4) 70%,
                transparent 100%);
            clip-path: polygon(0% 0%, 100% 50%, 0% 100%);
        }

        .spaceship-engine {
            position: absolute;
            right: -15px;
            top: 50%;
            transform: translateY(-50%);
            width: 30px;
            height: 15px;
            background: radial-gradient(circle, 
                rgba(255, 100, 100, 0.9) 0%,
                rgba(255, 50, 50, 0.8) 50%,
                transparent 70%);
            border-radius: 50%;
            animation: enginePulse 0.5s infinite alternate;
        }

        @keyframes enginePulse {
            0% { opacity: 0.5; transform: translateY(-50%) scale(0.8); }
            100% { opacity: 1; transform: translateY(-50%) scale(1.2); }
        }

        .engine-trail {
            position: absolute;
            right: -60px;
            top: 50%;
            transform: translateY(-50%);
            width: 50px;
            height: 4px;
            background: linear-gradient(90deg, 
                rgba(255, 50, 50, 0.8) 0%,
                rgba(255, 150, 50, 0.6) 30%,
                rgba(0, 243, 255, 0.3) 70%,
                transparent 100%);
            border-radius: 2px;
        }

        /* Shooting stars */
        .shooting-star {
            position: absolute;
            width: 2px;
            height: 2px;
            background: white;
            box-shadow: 0 0 10px 2px white;
            animation: shoot 3s linear infinite;
        }

        @keyframes shoot {
            0% { transform: translate(0, 0); opacity: 1; }
            100% { transform: translate(-300px, 300px); opacity: 0; }
        }

        .grid-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(var(--cyan-dark) 1px, transparent 1px),
                linear-gradient(90deg, var(--cyan-dark) 1px, transparent 1px);
            background-size: 50px 50px;
            opacity: 0.03;
            pointer-events: none;
            z-index: 1;
            animation: gridMove 20s linear infinite;
        }

        @keyframes gridMove {
            0% { transform: translateY(0); }
            100% { transform: translateY(50px); }
        }

        .scanline {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, var(--cyan-neon), transparent);
            opacity: 0.3;
            animation: scan 4s linear infinite;
            pointer-events: none;
            z-index: 9999;
        }

        @keyframes scan {
            0% { transform: translateY(0); }
            100% { transform: translateY(100vh); }
        }

        /* Login Screen */
        .login-screen {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            overflow-y: auto;
            padding: 20px 0;
            position: relative;
        }

        .login-container {
            background: rgba(13, 2, 33, 0.9);
            backdrop-filter: blur(10px);
            border: 2px solid var(--cyan-neon);
            box-shadow: var(--neon-glow), inset 0 0 20px rgba(0, 243, 255, 0.1);
            border-radius: 24px;
            padding: 40px 32px;
            width: 90%;
            max-width: 420px;
            max-height: 85vh;
            overflow-y: auto;
            text-align: center;
            margin: auto;
            animation: loginPulse 2s infinite alternate;
            position: relative;
            z-index: 100;
        }

        @keyframes loginPulse {
            0% { box-shadow: var(--neon-glow), inset 0 0 20px rgba(0, 243, 255, 0.1); }
            100% { box-shadow: 0 0 15px var(--cyan-neon), 0 0 30px var(--cyan-neon), 0 0 45px var(--cyan-neon), inset 0 0 30px rgba(0, 243, 255, 0.2); }
        }

        .app-icon {
            width: 120px;
            height: 120px;
            background: linear-gradient(135deg, var(--cyan-dark), var(--cyan-bright));
            border-radius: 22px;
            margin: 0 auto 20px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 48px;
            box-shadow: var(--neon-glow);
            border: 2px solid var(--cyan-neon);
            position: relative;
            overflow: hidden;
            animation: iconFloat 3s ease-in-out infinite;
        }

        @keyframes iconFloat {
            0%, 100% { transform: translateY(0px); }
            50% { transform: translateY(-10px); }
        }

        .app-icon::before {
            content: '';
            position: absolute;
            width: 100%;
            height: 100%;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><text y="70" font-size="60" fill="%23fff">🤖</text></svg>') no-repeat center;
            background-size: 70%;
            filter: drop-shadow(0 0 10px var(--cyan-neon));
        }

        .app-icon img {
            width: 80%;
            height: 80%;
            object-fit: contain;
            filter: drop-shadow(0 0 10px var(--cyan-neon));
            z-index: 1;
        }

        .login-title {
            font-size: 36px;
            font-weight: 700;
            background: linear-gradient(135deg, var(--cyan-neon), var(--cyan-bright));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
            text-shadow: 0 0 30px rgba(0, 243, 255, 0.5);
            animation: titleGlow 2s ease-in-out infinite;
        }

        @keyframes titleGlow {
            0%, 100% { filter: brightness(1); }
            50% { filter: brightness(1.3); }
        }

        .login-subtitle {
            font-size: 16px;
            color: var(--cyan-bright);
            margin-bottom: 28px;
            text-shadow: 0 0 10px rgba(107, 255, 255, 0.5);
        }

        .input-group {
            margin-bottom: 20px;
            text-align: left;
        }

        .text-input {
            width: 100%;
            padding: 14px 16px;
            border: 2px solid var(--cyan-dark);
            border-radius: 12px;
            font-size: 16px;
            transition: all 0.3s;
            background: rgba(13, 2, 33, 0.8);
            box-sizing: border-box;
            color: var(--cyan-bright);
        }

        .text-input:focus {
            outline: none;
            border-color: var(--cyan-neon);
            box-shadow: var(--neon-glow);
            background: rgba(13, 2, 33, 0.95);
        }

        .text-input::placeholder {
            color: rgba(107, 255, 255, 0.5);
        }

        .input-group small {
            font-size: 12px;
            color: var(--cyan-bright);
            display: block;
            margin-top: 6px;
        }

        .input-group small a {
            color: var(--cyan-neon);
            text-decoration: none;
        }

        .input-group small a:hover {
            text-decoration: underline;
            text-shadow: 0 0 10px var(--cyan-neon);
        }

        .login-note {
            font-size: 13px;
            color: var(--cyan-bright);
            margin-top: 16px;
            line-height: 1.4;
            opacity: 0.8;
        }

        .primary-btn {
            width: 100%;
            padding: 15px;
            background: linear-gradient(135deg, var(--cyan-dark), var(--cyan-bright));
            color: var(--purple-dark);
            border: 2px solid var(--cyan-neon);
            border-radius: 12px;
            font-size: 17px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.3s;
            margin-top: 8px;
            text-shadow: none;
            box-shadow: var(--neon-glow);
        }

        .primary-btn:hover {
            background: linear-gradient(135deg, var(--cyan-bright), var(--cyan-neon));
            transform: translateY(-2px);
            box-shadow: 0 0 15px var(--cyan-neon), 0 0 30px var(--cyan-neon), 0 0 45px var(--cyan-neon);
        }

        .primary-btn:active {
            transform: translateY(0);
        }

        /* Chat Screen */
        .chat-screen {
            display: none;
            flex-direction: column;
            height: 100vh;
            height: 100dvh;
            background: transparent;
            position: fixed;
            width: 100%;
            top: 0;
            left: 0;
            z-index: 100;
        }

        .chat-screen.active {
            display: flex;
        }

        .top-bar {
            background: rgba(13, 2, 33, 0.95);
            backdrop-filter: blur(10px);
            padding: 12px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
            border-bottom: 2px solid var(--cyan-dark);
            box-shadow: 0 0 20px rgba(0, 243, 255, 0.3);
        }

        .menu-btn {
            background: none;
            border: 2px solid var(--cyan-neon);
            font-size: 24px;
            cursor: pointer;
            padding: 8px;
            color: var(--cyan-neon);
            border-radius: 8px;
            text-shadow: 0 0 10px var(--cyan-neon);
            transition: all 0.3s;
        }

        .menu-btn:hover {
            background: rgba(0, 243, 255, 0.1);
            box-shadow: var(--neon-glow);
        }

        .app-title {
            flex: 1;
            font-size: 18px;
            font-weight: 700;
            background: linear-gradient(135deg, var(--cyan-neon), var(--cyan-bright));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .status-indicator {
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--cyan-neon);
            box-shadow: 0 0 10px var(--cyan-neon);
            animation: pulse 2s infinite;
        }

        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.5; }
        }

        .status-indicator.offline {
            background: #ff006e;
            box-shadow: 0 0 10px #ff006e;
        }

        .quick-actions {
            display: flex;
            gap: 8px;
            padding: 8px 16px;
            background: rgba(13, 2, 33, 0.95);
            border-bottom: 1px solid var(--cyan-dark);
            overflow-x: auto;
            -webkit-overflow-scrolling: touch;
        }

        .quick-actions::-webkit-scrollbar {
            height: 4px;
        }

        .quick-actions::-webkit-scrollbar-thumb {
            background: var(--cyan-dark);
            border-radius: 2px;
        }

        .quick-action-btn {
            padding: 8px 16px;
            background: rgba(0, 168, 181, 0.1);
            border: 1px solid var(--cyan-dark);
            border-radius: 20px;
            color: var(--cyan-bright);
            font-size: 14px;
            white-space: nowrap;
            cursor: pointer;
            transition: all 0.3s;
        }

        .quick-action-btn:hover {
            background: rgba(0, 168, 181, 0.2);
            border-color: var(--cyan-neon);
            box-shadow: 0 0 10px rgba(0, 243, 255, 0.3);
            transform: translateY(-2px);
        }

        .quick-action-btn:active {
            transform: translateY(0);
        }

        .chat-container {
            flex: 1;
            overflow-y: auto;
            overflow-x: hidden;
            padding: 16px;
            display: flex;
            flex-direction: column;
            gap: 8px;
            -webkit-overflow-scrolling: touch;
            min-height: 0;
            position: relative;
            backdrop-filter: blur(2px);
        }

        .chat-container::-webkit-scrollbar {
            width: 8px;
        }

        .chat-container::-webkit-scrollbar-track {
            background: rgba(0, 168, 181, 0.1);
            border-radius: 4px;
        }

        .chat-container::-webkit-scrollbar-thumb {
            background: var(--cyan-dark);
            border-radius: 4px;
            border: 2px solid transparent;
        }

        .chat-container::-webkit-scrollbar-thumb:hover {
            background: var(--cyan-neon);
            box-shadow: 0 0 10px var(--cyan-neon);
        }

        @keyframes messageSlideIn {
            from {
                opacity: 0;
                transform: translateY(20px) scale(0.95);
            }
            to {
                opacity: 1;
                transform: translateY(0) scale(1);
            }
        }

        .message-bubble {
            max-width: 80%;
            padding: 12px 16px;
            border-radius: 18px;
            font-size: 15px;
            line-height: 1.4;
            word-wrap: break-word;
            position: relative;
            transition: all 0.3s;
            animation: messageSlideIn 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .message-bubble:hover {
            transform: translateY(-2px);
            filter: brightness(1.1);
        }

        .message-bubble.user {
            background: linear-gradient(135deg, var(--cyan-dark), var(--cyan-bright));
            color: var(--purple-dark);
            align-self: flex-end;
            border-bottom-right-radius: 4px;
            border: 1px solid var(--cyan-neon);
            box-shadow: 0 0 15px rgba(0, 243, 255, 0.3);
            font-weight: 500;
        }

        .message-bubble.assistant {
            background: rgba(13, 2, 33, 0.8);
            backdrop-filter: blur(10px);
            color: var(--cyan-bright);
            align-self: flex-start;
            border-bottom-left-radius: 4px;
            border: 1px solid var(--cyan-dark);
            box-shadow: 0 0 10px rgba(0, 243, 255, 0.2);
        }

        .input-area {
            background: rgba(13, 2, 33, 0.95);
            backdrop-filter: blur(10px);
            padding: 8px 12px;
            padding-bottom: max(8px, env(safe-area-inset-bottom));
            display: flex;
            gap: 8px;
            align-items: flex-end;
            border-top: 2px solid var(--cyan-dark);
            flex-shrink: 0;
            position: relative;
            z-index: 100;
            box-shadow: 0 0 20px rgba(0, 243, 255, 0.2);
        }

        .message-input-wrapper {
            flex: 1;
            background: rgba(0, 168, 181, 0.1);
            border: 1px solid var(--cyan-dark);
            border-radius: 20px;
            padding: 10px 16px;
            display: flex;
            align-items: center;
            min-height: 40px;
            max-height: 120px;
            overflow-y: auto;
            transition: all 0.3s;
        }

        .message-input-wrapper:focus-within {
            border-color: var(--cyan-neon);
            box-shadow: 0 0 15px rgba(0, 243, 255, 0.3);
            background: rgba(0, 168, 181, 0.15);
        }

        .message-input {
            flex: 1;
            border: none;
            background: none;
            font-size: 16px;
            resize: none;
            font-family: inherit;
            line-height: 1.4;
            min-height: 20px;
            max-height: 96px;
            overflow-y: auto;
            width: 100%;
            color: var(--cyan-bright);
        }

        .message-input:focus {
            outline: none;
        }

        .message-input::placeholder {
            color: rgba(107, 255, 255, 0.5);
        }

        .send-btn {
            width: 36px;
            height: 36px;
            min-width: 36px;
            min-height: 36px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--cyan-dark), var(--cyan-bright));
            border: 2px solid var(--cyan-neon);
            color: var(--purple-dark);
            font-size: 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s;
            flex-shrink: 0;
            box-shadow: var(--neon-glow);
            font-weight: bold;
        }

        .send-btn:hover {
            transform: scale(1.1);
            box-shadow: 0 0 20px var(--cyan-neon), 0 0 40px var(--cyan-neon);
        }

        .send-btn:active {
            transform: scale(0.95);
        }

        .menu-overlay {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(0, 0, 0, 0.4);
            display: none;
            z-index: 999;
        }

        .menu-overlay.active {
            display: block;
            animation: fadeIn 0.3s ease;
        }

        @keyframes fadeIn {
            from { opacity: 0; }
            to { opacity: 1; }
        }

        .side-menu {
            position: fixed;
            top: 0;
            left: -300px;
            width: 300px;
            height: 100%;
            background: rgba(13, 2, 33, 0.98);
            backdrop-filter: blur(20px);
            border-right: 2px solid var(--cyan-dark);
            box-shadow: 0 0 30px rgba(0, 243, 255, 0.3);
            z-index: 1000;
            transition: left 0.3s ease;
            overflow-y: auto;
            padding: 60px 20px 20px;
        }

        .side-menu.active {
            left: 0;
        }

        .user-profile {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 24px;
            padding-bottom: 24px;
            border-bottom: 1px solid var(--cyan-dark);
        }

        .user-avatar {
            width: 60px;
            height: 60px;
            border-radius: 50%;
            background: linear-gradient(135deg, var(--cyan-dark), var(--cyan-bright));
            border: 2px solid var(--cyan-neon);
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--purple-dark);
            font-size: 24px;
            font-weight: 700;
            box-shadow: var(--neon-glow);
        }

        .user-info h3 {
            font-size: 18px;
            font-weight: 700;
            color: var(--cyan-neon);
            text-shadow: 0 0 10px var(--cyan-neon);
        }

        .user-info p {
            font-size: 14px;
            color: var(--cyan-bright);
            opacity: 0.8;
        }

        .menu-section {
            margin-bottom: 24px;
        }

        .menu-section-title {
            font-size: 13px;
            font-weight: 700;
            color: var(--cyan-neon);
            text-transform: uppercase;
            margin-bottom: 12px;
            letter-spacing: 0.5px;
            text-shadow: 0 0 10px rgba(0, 243, 255, 0.5);
        }

        .menu-btn-item {
            width: 100%;
            padding: 12px 16px;
            background: rgba(0, 168, 181, 0.1);
            border: 1px solid var(--cyan-dark);
            border-radius: 10px;
            text-align: left;
            font-size: 15px;
            color: var(--cyan-bright);
            cursor: pointer;
            margin-bottom: 8px;
            transition: all 0.2s;
        }

        .menu-btn-item:hover {
            background: rgba(0, 168, 181, 0.2);
            border-color: var(--cyan-neon);
            transform: translateX(4px);
            box-shadow: 0 0 15px rgba(0, 243, 255, 0.3);
        }

        .menu-btn-item.danger {
            color: #ff006e;
            border-color: #ff006e;
        }

        .menu-btn-item.danger:hover {
            background: rgba(255, 0, 110, 0.1);
            box-shadow: 0 0 15px rgba(255, 0, 110, 0.3);
        }

        .menu-btn-item.install-btn {
            background: linear-gradient(135deg, rgba(0, 168, 181, 0.3), rgba(0, 243, 255, 0.2));
            border: 1px solid var(--cyan-neon);
            color: var(--cyan-neon);
            text-shadow: 0 0 10px var(--cyan-neon);
        }

        .menu-btn-item.install-btn:hover {
            background: linear-gradient(135deg, rgba(0, 168, 181, 0.4), rgba(0, 243, 255, 0.3));
            box-shadow: var(--neon-glow);
        }

        .settings-card {
            background: rgba(0, 168, 181, 0.1);
            border: 1px solid var(--cyan-dark);
            border-radius: 12px;
            padding: 12px 16px;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            transition: all 0.3s;
        }

        .settings-card:hover {
            background: rgba(0, 168, 181, 0.15);
            border-color: var(--cyan-neon);
            box-shadow: 0 0 15px rgba(0, 243, 255, 0.2);
        }

        .settings-label {
            font-size: 15px;
            color: var(--cyan-bright);
        }

        .switch {
            position: relative;
            width: 51px;
            height: 31px;
        }

        .switch input {
            opacity: 0;
            width: 0;
            height: 0;
        }

        .slider {
            position: absolute;
            cursor: pointer;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background-color: rgba(0, 168, 181, 0.2);
            transition: .4s;
            border-radius: 31px;
            border: 1px solid var(--cyan-dark);
        }

        .slider:before {
            position: absolute;
            content: "";
            height: 27px;
            width: 27px;
            left: 2px;
            bottom: 2px;
            background-color: var(--cyan-bright);
            transition: .4s;
            border-radius: 50%;
        }

        input:checked + .slider {
            background-color: var(--cyan-neon);
            box-shadow: 0 0 15px var(--cyan-neon);
        }

        input:checked + .slider:before {
            transform: translateX(20px);
        }

        .range-slider {
            width: 100%;
            height: 6px;
            border-radius: 3px;
            background: rgba(0, 168, 181, 0.2);
            outline: none;
            -webkit-appearance: none;
        }

        .range-slider::-webkit-slider-thumb {
            -webkit-appearance: none;
            appearance: none;
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: var(--cyan-neon);
            cursor: pointer;
            box-shadow: 0 0 10px var(--cyan-neon);
            transition: all 0.3s;
        }

        .range-slider::-webkit-slider-thumb:hover {
            transform: scale(1.2);
            box-shadow: 0 0 20px var(--cyan-neon);
        }

        .range-slider::-moz-range-thumb {
            width: 20px;
            height: 20px;
            border-radius: 50%;
            background: var(--cyan-neon);
            cursor: pointer;
            border: none;
            box-shadow: 0 0 10px var(--cyan-neon);
        }

        .hidden {
            display: none;
        }

        .api-dialog {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            background: rgba(13, 2, 33, 0.98);
            backdrop-filter: blur(20px);
            border: 2px solid var(--cyan-neon);
            box-shadow: var(--neon-glow);
            border-radius: 20px;
            padding: 24px;
            width: 90%;
            max-width: 400px;
            z-index: 2000;
            animation: dialogAppear 0.3s ease;
        }

        @keyframes dialogAppear {
            from {
                opacity: 0;
                transform: translate(-50%, -50%) scale(0.9);
            }
            to {
                opacity: 1;
                transform: translate(-50%, -50%) scale(1);
            }
        }

        .api-dialog h2 {
            font-size: 24px;
            font-weight: 700;
            background: linear-gradient(135deg, var(--cyan-neon), var(--cyan-bright));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            margin-bottom: 8px;
        }

        .api-dialog p {
            font-size: 14px;
            color: var(--cyan-bright);
            margin-bottom: 20px;
            opacity: 0.8;
        }

        .api-input-group {
            margin-bottom: 16px;
        }

        .api-input-group label {
            display: block;
            font-size: 14px;
            font-weight: 600;
            color: var(--cyan-neon);
            margin-bottom: 8px;
        }

        .api-input-group input {
            width: 100%;
            padding: 12px;
            border: 2px solid var(--cyan-dark);
            border-radius: 10px;
            font-size: 14px;
            font-family: monospace;
            background: rgba(0, 168, 181, 0.1);
            color: var(--cyan-bright);
            transition: all 0.3s;
        }

        .api-input-group input:focus {
            outline: none;
            border-color: var(--cyan-neon);
            box-shadow: var(--neon-glow);
            background: rgba(0, 168, 181, 0.15);
        }

        .api-input-group small {
            display: block;
            margin-top: 4px;
            font-size: 12px;
            color: var(--cyan-bright);
            opacity: 0.7;
        }

        .api-input-group small a {
            color: var(--cyan-neon);
            text-decoration: none;
        }

        .api-dialog-buttons {
            display: flex;
            gap: 8px;
            margin-top: 20px;
        }

        .api-dialog-buttons button {
            flex: 1;
            padding: 12px;
            border: none;
            border-radius: 10px;
            font-size: 16px;
            font-weight: 600;
            cursor: pointer;
        }

        .btn-save {
            background: linear-gradient(135deg, var(--cyan-dark), var(--cyan-bright));
            color: var(--purple-dark);
            border: 2px solid var(--cyan-neon);
            box-shadow: var(--neon-glow);
        }

        .btn-save:hover {
            box-shadow: 0 0 20px var(--cyan-neon), 0 0 40px var(--cyan-neon);
            transform: translateY(-2px);
        }

        .btn-cancel {
            background: rgba(0, 168, 181, 0.1);
            color: var(--cyan-bright);
            border: 1px solid var(--cyan-dark);
        }

        .btn-cancel:hover {
            background: rgba(0, 168, 181, 0.2);
        }

        .api-status {
            display: inline-block;
            padding: 4px 8px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            margin-left: 8px;
        }

        .api-status.configured {
            background: var(--cyan-neon);
            color: var(--purple-dark);
            box-shadow: 0 0 10px var(--cyan-neon);
        }

        .api-status.not-configured {
            background: rgba(255, 0, 110, 0.3);
            color: #ff006e;
            border: 1px solid #ff006e;
        }

        .typing-indicator {
            display: flex;
            gap: 4px;
            padding: 12px 16px;
            background: rgba(13, 2, 33, 0.8);
            backdrop-filter: blur(10px);
            border: 1px solid var(--cyan-dark);
            border-radius: 18px;
            width: fit-content;
            border-bottom-left-radius: 4px;
        }

        .typing-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--cyan-neon);
            box-shadow: 0 0 10px var(--cyan-neon);
            animation: typing 1.4s infinite;
        }

        .typing-dot:nth-child(2) {
            animation-delay: 0.2s;
        }

        .typing-dot:nth-child(3) {
            animation-delay: 0.4s;
        }

        @keyframes typing {
            0%, 60%, 100% {
                transform: translateY(0);
                opacity: 0.7;
            }
            30% {
                transform: translateY(-10px);
                opacity: 1;
            }
        }

        .install-status {
            padding: 8px 12px;
            margin: 8px 0;
            border-radius: 8px;
            font-size: 13px;
            text-align: center;
        }

        .install-status.installed {
            background: rgba(0, 243, 255, 0.1);
            color: var(--cyan-neon);
            border: 1px solid var(--cyan-neon);
        }

        .install-status.available {
            background: rgba(157, 78, 221, 0.1);
            color: #9d4edd;
            border: 1px solid #9d4edd;
        }

        .install-status.not-available {
            background: rgba(255, 0, 110, 0.1);
            color: #ff006e;
            border: 1px solid #ff006e;
        }

        /* Install Prompt Popup */
        .install-popup {
            position: fixed;
            bottom: 20px;
            right: 20px;
            background: rgba(13, 2, 33, 0.95);
            backdrop-filter: blur(20px);
            border: 2px solid var(--cyan-neon);
            box-shadow: var(--neon-glow);
            border-radius: 16px;
            padding: 20px;
            width: 300px;
            z-index: 9998;
            animation: slideIn 0.5s ease;
            display: none;
        }

        @keyframes slideIn {
            from {
                opacity: 0;
                transform: translateX(100px);
            }
            to {
                opacity: 1;
                transform: translateX(0);
            }
        }

        .install-popup-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 12px;
        }

        .install-popup-icon {
            font-size: 24px;
            color: var(--cyan-neon);
        }

        .install-popup-title {
            font-size: 18px;
            font-weight: 700;
            color: var(--cyan-neon);
            flex: 1;
        }

        .install-popup-close {
            background: none;
            border: none;
            color: var(--cyan-bright);
            font-size: 20px;
            cursor: pointer;
            padding: 4px;
            border-radius: 50%;
            width: 28px;
            height: 28px;
            display: flex;
            align-items: center;
            justify-content: center;
        }

        .install-popup-close:hover {
            background: rgba(0, 243, 255, 0.1);
        }

        .install-popup-body {
            color: var(--cyan-bright);
            font-size: 14px;
            line-height: 1.5;
            margin-bottom: 20px;
        }

        .install-popup-buttons {
            display: flex;
            gap: 10px;
        }

        .install-popup-btn {
            flex: 1;
            padding: 10px;
            border: none;
            border-radius: 10px;
            font-weight: 600;
            cursor: pointer;
            font-size: 14px;
        }

        .install-popup-btn.primary {
            background: linear-gradient(135deg, var(--cyan-dark), var(--cyan-bright));
            color: var(--purple-dark);
            border: 1px solid var(--cyan-neon);
        }

        .install-popup-btn.secondary {
            background: rgba(0, 168, 181, 0.1);
            color: var(--cyan-bright);
            border: 1px solid var(--cyan-dark);
        }
    </style>
</head>
<body>
    <!-- Milky Way Galaxy Background -->
    <div class="galaxy-background">
        <div class="galaxy-core"></div>
        <div class="galaxy-arm arm-1"></div>
        <div class="galaxy-arm arm-2"></div>
        <div class="galaxy-arm arm-3"></div>
        <div class="stars" id="starsContainer"></div>
        <div id="spaceshipsContainer"></div>
        <div class="shooting-star" style="top: 20%; right: 80%; animation-delay: 0s;"></div>
        <div class="shooting-star" style="top: 50%; right: 60%; animation-delay: 2s;"></div>
        <div class="shooting-star" style="top: 70%; right: 40%; animation-delay: 4s;"></div>
        <div class="grid-overlay"></div>
    </div>
    
    <!-- Scan line effect -->
    <div class="scanline"></div>

    <!-- Install Prompt Popup -->
    <div id="installPopup" class="install-popup">
        <div class="install-popup-header">
            <div class="install-popup-icon">📲</div>
            <div class="install-popup-title">Install Cyanix AI</div>
            <button class="install-popup-close" onclick="hideInstallPopup()">×</button>
        </div>
        <div class="install-popup-body">
            Install Cyanix AI on your home screen for quick access and offline use. 
            Works just like a native app!
        </div>
        <div class="install-popup-buttons">
            <button class="install-popup-btn secondary" onclick="hideInstallPopup()">Later</button>
            <button class="install-popup-btn primary" onclick="installPWA()">Install Now</button>
        </div>
    </div>

    <!-- Login Screen -->
    <div id="loginScreen" class="login-screen">
        <div class="login-container">
            <div class="app-icon">
                <img src="cyanix_emblem.png" alt="Cyanix" onerror="this.style.display='none'" />
            </div>
            <h1 class="login-title">Cyanix AI</h1>
            <p class="login-subtitle">Your intelligent assistant</p>
            
            <div class="input-group">
                <input type="password" id="apiKeyLoginInput" class="text-input" placeholder="Enter your Groq API Key" autocomplete="off" />
                <small>
                    Get free key at <a href="https://console.groq.com" target="_blank">console.groq.com</a>
                </small>
                <small style="display: block; margin-top: 8px; color: var(--cyan-neon); font-weight: 600;">
                    ⚠️ Your API key is your password - stored locally and never shared
                </small>
            </div>
            
            <button class="primary-btn" onclick="login()">Enter Cyanix AI</button>
            
            <p class="login-note">
                🔐 Fully private - no data saved, no tracking, no accounts
            </p>
        </div>
    </div>

    <!-- Chat Screen -->
    <div id="chatScreen" class="chat-screen">
        <div class="top-bar">
            <button class="menu-btn" onclick="toggleMenu()">☰</button>
            <div class="app-title">Cyanix AI</div>
            <div class="status-indicator" id="statusIndicator"></div>
        </div>

        <!-- Quick Actions Toolbar -->
        <div class="quick-actions">
            <button class="quick-action-btn" onclick="sendQuickMessage('Explain this concept simply')">💡 Explain</button>
            <button class="quick-action-btn" onclick="sendQuickMessage('Help me brainstorm ideas')">🧠 Brainstorm</button>
            <button class="quick-action-btn" onclick="sendQuickMessage('Write code for')">💻 Code</button>
            <button class="quick-action-btn" onclick="sendQuickMessage('Analyze this')">📊 Analyze</button>
            <button class="quick-action-btn" onclick="sendQuickMessage('Summarize')">📝 Summarize</button>
            <button class="quick-action-btn" onclick="sendQuickMessage('Tell me a joke')">😄 Joke</button>
        </div>

        <div class="chat-container" id="chatContainer"></div>

        <div class="input-area">
            <div class="message-input-wrapper">
                <textarea 
                    id="messageInput" 
                    class="message-input" 
                    placeholder="Message" 
                    rows="1"
                    oninput="autoResizeInput(this)"
                    onkeydown="handleKeyDown(event)"
                ></textarea>
            </div>
            <button class="send-btn" onclick="sendMessage()">↑</button>
        </div>
    </div>

    <!-- Side Menu -->
    <div id="menuOverlay" class="menu-overlay" onclick="toggleMenu()"></div>
    <div id="sideMenu" class="side-menu">
        <div class="user-profile">
            <div class="user-avatar">C</div>
            <div class="user-info">
                <h3>Cyanix User</h3>
                <p>Anonymous Session</p>
            </div>
        </div>

        <div class="menu-section">
            <div class="menu-section-title">AI Mode</div>
            <button class="menu-btn-item" onclick="setAIMode('nix')">⚡ Nix - Quick Responses</button>
            <button class="menu-btn-item" onclick="setAIMode('default')">🤖 Cyanix - Balanced</button>
            <button class="menu-btn-item" onclick="setAIMode('nova')">🧠 Nova - Deep Thinking</button>
        </div>

        <div class="menu-section">
            <div class="menu-section-title">Settings</div>
            <div class="settings-card">
                <span class="settings-label">Auto-Speak</span>
                <label class="switch">
                    <input type="checkbox" id="autoSpeakToggle" checked onchange="toggleAutoSpeak()">
                    <span class="slider"></span>
                </label>
            </div>
            <div class="settings-card">
                <span class="settings-label">Voice Speed</span>
                <input type="range" class="range-slider" min="50" max="150" value="90" id="voiceSpeedSlider">
            </div>
        </div>

        <div class="menu-section">
            <div class="menu-section-title">API Keys</div>
            <button class="menu-btn-item" onclick="showAPIKeyDialog()">🔑 Configure API Keys</button>
        </div>

        <div class="menu-section">
            <div class="menu-section-title">App Installation</div>
            <div id="installStatus" class="install-status not-available">Checking installation status...</div>
            <button class="menu-btn-item install-btn" onclick="installPWA()" id="installBtn" style="display: none;">
                📲 Install Cyanix AI
            </button>
            <button class="menu-btn-item" onclick="showInstallInstructions()">📋 Installation Guide</button>
        </div>

        <div class="menu-section">
            <button class="menu-btn-item danger" onclick="logout()">🚪 Logout</button>
        </div>
    </div>

    <!-- API Key Configuration Dialog -->
    <div id="apiKeyDialog" class="menu-overlay hidden">
        <div class="api-dialog">
            <h2>Configure API Keys</h2>
            <p>Enter your API keys to enable AI responses. Keys are stored locally in your browser.</p>
            
            <div class="api-input-group">
                <label>
                    Groq API Key 
                    <span class="api-status" id="groqStatus">Not Configured</span>
                </label>
                <input type="password" id="groqKeyInput" placeholder="gsk_..." autocomplete="off" />
                <small>Get free key at <a href="https://console.groq.com" target="_blank">console.groq.com</a></small>
                <small style="display: block; margin-top: 4px; color: #ff006e; font-weight: 600;">
                    ⚠️ Make sure to copy the FULL key (starts with gsk_)
                </small>
            </div>

            <div class="api-input-group">
                <label>
                    Anthropic API Key (Optional)
                    <span class="api-status" id="anthropicStatus">Not Configured</span>
                </label>
                <input type="password" id="anthropicKeyInput" placeholder="sk-ant-..." autocomplete="off" />
                <small>Get key at <a href="https://console.anthropic.com" target="_blank">console.anthropic.com</a></small>
            </div>

            <div class="api-dialog-buttons">
                <button class="btn-cancel" onclick="closeAPIKeyDialog()">Cancel</button>
                <button class="btn-save" onclick="saveAPIKeys()">Save Keys</button>
            </div>
        </div>
    </div>

    <script>
        // Generate Milky Way Galaxy
        function createGalaxy() {
            createStars();
            createSpaceships();
        }

        // Generate animated stars
        function createStars() {
            const container = document.getElementById('starsContainer');
            const starCount = 300;
            
            for (let i = 0; i < starCount; i++) {
                const star = document.createElement('div');
                const size = Math.random();
                if (size > 0.7) {
                    star.className = 'star large';
                } else if (size > 0.4) {
                    star.className = 'star medium';
                } else {
                    star.className = 'star small';
                }
                
                star.style.left = Math.random() * 100 + '%';
                star.style.top = Math.random() * 100 + '%';
                star.style.animationDelay = Math.random() * 3 + 's';
                star.style.animationDuration = (Math.random() * 3 + 2) + 's';
                container.appendChild(star);
            }
        }

        // Generate spaceships
        function createSpaceships() {
            const container = document.getElementById('spaceshipsContainer');
            const shipCount = 5;
            
            for (let i = 0; i < shipCount; i++) {
                const spaceship = document.createElement('div');
                const size = Math.random();
                
                if (size > 0.7) {
                    spaceship.className = 'spaceship large';
                } else if (size > 0.4) {
                    spaceship.className = 'spaceship medium';
                } else {
                    spaceship.className = 'spaceship small';
                }
                
                // Create spaceship parts
                const body = document.createElement('div');
                body.className = 'spaceship-body';
                
                const wings = document.createElement('div');
                wings.className = 'spaceship-wings';
                
                const engine = document.createElement('div');
                engine.className = 'spaceship-engine';
                
                const trail = document.createElement('div');
                trail.className = 'engine-trail';
                
                spaceship.appendChild(body);
                spaceship.appendChild(wings);
                spaceship.appendChild(engine);
                spaceship.appendChild(trail);
                
                // Random starting position
                const startX = -100;
                const startY = Math.random() * 100;
                
                // Random flight path
                const endX = 100 + Math.random() * 50;
                const endY = startY + (Math.random() * 40 - 20);
                
                // Random speed
                const duration = 20 + Math.random() * 30;
                const delay = Math.random() * 30;
                
                // Set initial position
                spaceship.style.left = startX + 'px';
                spaceship.style.top = startY + 'vh';
                
                // Animate
                spaceship.style.animation = `
                    flyShip ${duration}s linear ${delay}s infinite
                `;
                
                // Define keyframes for this ship
                const style = document.createElement('style');
                style.textContent = `
                    @keyframes flyShip-${i} {
                        0% {
                            transform: translate(0, 0) rotate(0deg);
                            opacity: 0;
                        }
                        10% {
                            opacity: 1;
                        }
                        90% {
                            opacity: 1;
                        }
                        100% {
                            transform: translate(${endX}vw, ${endY}vh) rotate(${Math.random() * 360}deg);
                            opacity: 0;
                        }
                    }
                `;
                document.head.appendChild(style);
                
                spaceship.style.animation = `flyShip-${i} ${duration}s linear ${delay}s infinite`;
                container.appendChild(spaceship);
            }
        }

        // Initialize galaxy on load
        window.addEventListener('load', function() {
            createGalaxy();
        });

        // Main Application Variables
        let currentUser = '';
        let chatHistory = [];
        let currentMode = 'default';
        let autoSpeak = true;
        let isOnline = true;
        let menuOpen = false;
        let deferredPrompt = null;
        let isAppInstalled = false;

        // Personality
        const PERSONALITY = `You are Cyanix AI, a highly intelligent and helpful assistant.

Core Traits:
- Friendly, approachable, and conversational
- Clear and concise in explanations
- Patient and understanding
- Proactive in offering help
- Professional yet warm

Communication Style:
- Use natural, everyday language
- Avoid overly technical jargon unless requested
- Be encouraging and positive
- Show empathy and understanding
- Adapt tone to match the user's mood

Capabilities:
- Answer questions on a wide range of topics
- Help with problem-solving and decision-making
- Provide explanations and tutorials
- Assist with creative tasks and brainstorming
- Offer practical advice and recommendations

Remember:
- You're here to help and support the user
- Be honest when you don't know something
- Maintain a helpful and respectful demeanor
- Focus on being genuinely useful`;

        // API Configuration
        const API_CONFIG = {
            groq: {
                key: localStorage.getItem('groq_api_key') || '',
                endpoint: 'https://api.groq.com/openai/v1/chat/completions',
                models: {
                    nix: 'llama-3.1-8b-instant',
                    default: 'llama-3.3-70b-versatile',
                    nova: 'llama-3.3-70b-versatile'
                }
            },
            anthropic: {
                key: localStorage.getItem('anthropic_api_key') || '',
                endpoint: 'https://api.anthropic.com/v1/messages',
                model: 'claude-sonnet-4-20250514'
            }
        };

        // Check online status
        setInterval(() => {
            isOnline = navigator.onLine;
            const indicator = document.getElementById('statusIndicator');
            if (indicator) {
                if (isOnline) {
                    indicator.classList.remove('offline');
                } else {
                    indicator.classList.add('offline');
                }
            }
        }, 5000);

        // =============== PWA Installation Functions ===============
        function checkIfPWAInstalled() {
            if (window.matchMedia('(display-mode: standalone)').matches) return true;
            if (window.navigator.standalone === true) return true;
            if (document.referrer.includes('android-app://')) return true;
            return false;
        }

        function updateInstallStatus() {
            const installBtn = document.getElementById('installBtn');
            const installStatus = document.getElementById('installStatus');
            
            isAppInstalled = checkIfPWAInstalled();
            
            if (isAppInstalled) {
                installStatus.innerHTML = '✅ Cyanix AI is installed';
                installStatus.className = 'install-status installed';
                if (installBtn) installBtn.style.display = 'none';
            } else if (deferredPrompt) {
                installStatus.innerHTML = '📲 Available for installation';
                installStatus.className = 'install-status available';
                if (installBtn) installBtn.style.display = 'block';
            } else {
                installStatus.innerHTML = 'ℹ️ Visit in Chrome/Safari to install';
                installStatus.className = 'install-status not-available';
                if (installBtn) installBtn.style.display = 'none';
            }
        }

        // Listen for install prompt
        window.addEventListener('beforeinstallprompt', (e) => {
            console.log('📲 PWA install prompt available');
            e.preventDefault();
            deferredPrompt = e;
            updateInstallStatus();
            
            // Show automatic popup after 3 seconds
            setTimeout(() => {
                const lastHide = localStorage.getItem('hideInstallPopup');
                const oneDay = 24 * 60 * 60 * 1000;
                
                if (!lastHide || (Date.now() - lastHide > oneDay)) {
                    if (!isAppInstalled && deferredPrompt) {
                        showInstallPopup();
                    }
                }
            }, 3000);
        });

        // Listen for app installed event
        window.addEventListener('appinstalled', () => {
            console.log('🎉 Cyanix AI was installed');
            isAppInstalled = true;
            updateInstallStatus();
        });

        // Main install function
        function installPWA() {
            if (!deferredPrompt) {
                showInstallInstructions();
                return;
            }
            
            deferredPrompt.prompt();
            
            deferredPrompt.userChoice.then((choiceResult) => {
                if (choiceResult.outcome === 'accepted') {
                    console.log('✅ User accepted installation');
                    
                    // Update status
                    const installStatus = document.getElementById('installStatus');
                    installStatus.innerHTML = '🎉 Installing... Check home screen!';
                    installStatus.className = 'install-status installed';
                    
                    // Hide install button
                    const installBtn = document.getElementById('installBtn');
                    if (installBtn) installBtn.style.display = 'none';
                    
                    // Close popup if open
                    hideInstallPopup();
                } else {
                    console.log('❌ User dismissed installation');
                }
                
                deferredPrompt = null;
                updateInstallStatus();
            });
        }

        // Install popup functions
        function showInstallPopup() {
            const popup = document.getElementById('installPopup');
            if (popup) popup.style.display = 'block';
        }

        function hideInstallPopup() {
            const popup = document.getElementById('installPopup');
            if (popup) popup.style.display = 'none';
            localStorage.setItem('hideInstallPopup', Date.now());
        }

        function showInstallInstructions() {
            const platform = detectPlatform();
            let instructions = '';
            
            switch(platform) {
                case 'ios':
                    instructions = `
                        <strong>On iPhone/iPad:</strong><br>
                        1. Tap the <strong>Share button</strong> (📤)<br>
                        2. Scroll down, tap <strong>"Add to Home Screen"</strong><br>
                        3. Tap <strong>"Add"</strong> in top right
                    `;
                    break;
                    
                case 'android':
                    instructions = `
                        <strong>On Android:</strong><br>
                        1. Tap the <strong>three dots menu</strong> (⋮)<br>
                        2. Tap <strong>"Install app"</strong><br>
                        3. Tap <strong>"Install"</strong>
                    `;
                    break;
                    
                case 'desktop':
                    instructions = `
                        <strong>On Desktop:</strong><br>
                        Look for the <strong>"➕" install icon</strong> in the address bar
                    `;
                    break;
            }
            
            alert(`How to install Cyanix AI:\n\n${instructions.replace(/<br>/g, '\n').replace(/<strong>|<\/strong>/g, '')}`);
        }

        function detectPlatform() {
            const userAgent = navigator.userAgent.toLowerCase();
            if (/iphone|ipad|ipod/.test(userAgent)) return 'ios';
            if (/android/.test(userAgent)) return 'android';
            return 'desktop';
        }

        // Initialize PWA status
        document.addEventListener('DOMContentLoaded', function() {
            setTimeout(updateInstallStatus, 1000);
            setTimeout(updateInstallStatus, 3000);
        });

        // =============== Main App Functions ===============
        function login() {
            const apiKey = document.getElementById('apiKeyLoginInput').value.trim();
            
            if (!apiKey) {
                alert('Please enter your Groq API key to continue');
                return;
            }

            if (!apiKey.startsWith('gsk_')) {
                alert('Invalid API key format. Groq keys start with "gsk_"');
                return;
            }

            localStorage.setItem('groq_api_key', apiKey);
            API_CONFIG.groq.key = apiKey;
            currentUser = 'Anonymous User';
            
            document.getElementById('loginScreen').style.display = 'none';
            document.getElementById('chatScreen').classList.add('active');
            testAPIKeyOnLogin();
        }

        async function testAPIKeyOnLogin() {
            addMessage('🔐 Authenticating with Cyanix AI...', false);
            
            try {
                const response = await fetch(API_CONFIG.groq.endpoint, {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${API_CONFIG.groq.key}`,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        model: 'llama-3.1-8b-instant',
                        messages: [
                            { role: 'user', content: 'Hi' }
                        ],
                        max_tokens: 50
                    })
                });

                if (response.ok) {
                    const greeting = `✅ Welcome to Cyanix AI! Your connection is secure. How can I assist you today?`;
                    addMessage(greeting, false);
                    speak(greeting);
                } else {
                    const errorText = await response.text();
                    let errorMsg = 'Unknown error';
                    try {
                        const errorData = JSON.parse(errorText);
                        errorMsg = errorData.error?.message || errorData.message || errorMsg;
                    } catch (e) {
                        errorMsg = errorText;
                    }
                    
                    if (response.status === 401) {
                        addMessage('❌ Invalid API key. Please logout and enter a valid Groq API key. Get one at console.groq.com', false);
                    } else {
                        addMessage(`⚠️ API Warning (${response.status}): ${errorMsg}. You can still try to chat.`, false);
                    }
                }
            } catch (error) {
                addMessage(`⚠️ Connection test failed: ${error.message}. You can still try to chat.`, false);
            }
        }

        function logout() {
            localStorage.removeItem('groq_api_key');
            API_CONFIG.groq.key = '';
            
            currentUser = '';
            chatHistory = [];
            document.getElementById('chatContainer').innerHTML = '';
            document.getElementById('apiKeyLoginInput').value = '';
            document.getElementById('chatScreen').classList.remove('active');
            document.getElementById('loginScreen').style.display = 'flex';
            if (menuOpen) {
                toggleMenu();
            }
        }

        function toggleMenu() {
            const overlay = document.getElementById('menuOverlay');
            const menu = document.getElementById('sideMenu');
            
            if (menuOpen) {
                overlay.classList.remove('active');
                menu.classList.remove('active');
                menuOpen = false;
            } else {
                overlay.classList.add('active');
                menu.classList.add('active');
                menuOpen = true;
            }
        }

        function addMessage(text, isUser = false) {
            const container = document.getElementById('chatContainer');
            const bubble = document.createElement('div');
            bubble.className = `message-bubble ${isUser ? 'user' : 'assistant'}`;
            bubble.textContent = text;
            container.appendChild(bubble);
            
            setTimeout(() => {
                container.scrollTo({
                    top: container.scrollHeight,
                    behavior: 'smooth'
                });
            }, 100);

            chatHistory.push({ text, isUser, timestamp: Date.now() });
        }

        function sendQuickMessage(prompt) {
            const input = document.getElementById('messageInput');
            input.value = prompt;
            input.focus();
            
            const wrapper = input.parentElement;
            wrapper.style.borderColor = 'var(--cyan-neon)';
            wrapper.style.boxShadow = '0 0 20px rgba(0, 243, 255, 0.5)';
            setTimeout(() => {
                wrapper.style.borderColor = '';
                wrapper.style.boxShadow = '';
            }, 1000);
        }

        function showTypingIndicator() {
            const container = document.getElementById('chatContainer');
            const indicator = document.createElement('div');
            indicator.className = 'typing-indicator';
            indicator.id = 'typingIndicator';
            indicator.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';
            container.appendChild(indicator);
            container.scrollTop = container.scrollHeight;
        }

        function hideTypingIndicator() {
            const indicator = document.getElementById('typingIndicator');
            if (indicator) indicator.remove();
        }

        async function sendMessage() {
            const input = document.getElementById('messageInput');
            const message = input.value.trim();
            if (!message) return;

            if (message.toLowerCase() === 'logout' || message.toLowerCase() === 'exit') {
                logout();
                return;
            }

            addMessage(message, true);
            input.value = '';
            
            input.style.height = 'auto';
            const wrapper = input.parentElement;
            wrapper.style.minHeight = '40px';
            wrapper.style.height = 'auto';

            showTypingIndicator();

            try {
                const response = await getAIResponse(message);
                hideTypingIndicator();
                addMessage(response, false);
                speak(response);
            } catch (error) {
                hideTypingIndicator();
                addMessage(`Error: ${error.message}. Please check your internet connection or API keys.`, false);
            }
        }

        async function getAIResponse(userMessage) {
            if (!API_CONFIG.groq.key && !API_CONFIG.anthropic.key) {
                throw new Error('No API keys configured. Please click "Configure API Keys" in the menu.');
            }

            const systemPrompt = `${PERSONALITY}

You are speaking to ${currentUser}. ${getModeInstructions()}`;
            
            const recentHistory = chatHistory.slice(-10).map(msg => ({
                role: msg.isUser ? 'user' : 'assistant',
                content: msg.text
            }));

            if (API_CONFIG.groq.key) {
                try {
                    return await callGroqAPI(systemPrompt, recentHistory, userMessage);
                } catch (error) {
                    console.error('Groq API failed:', error);
                }
            }
            
            if (API_CONFIG.anthropic.key) {
                try {
                    return await callAnthropicAPI(systemPrompt, recentHistory, userMessage);
                } catch (anthropicError) {
                    console.error('Anthropic API failed:', anthropicError);
                }
            }
            
            throw new Error('All API services unavailable. Please check your API keys.');
        }

        function getModeInstructions() {
            switch(currentMode) {
                case 'nix':
                    return 'You are in "Nix" mode: Respond quickly, concisely, and directly. Keep answers brief and to the point.';
                case 'nova':
                    return 'You are in "Nova" mode: Think deeply, provide detailed reasoning, explore possibilities, and give thorough, comprehensive answers.';
                default:
                    return 'You are in balanced mode: Provide helpful, clear, and well-structured responses.';
            }
        }

        async function callGroqAPI(systemPrompt, history, userMessage) {
            const model = API_CONFIG.groq.models[currentMode] || API_CONFIG.groq.models.default;
            
            const messages = [
                { role: 'system', content: systemPrompt },
                ...history,
                { role: 'user', content: userMessage }
            ];

            const response = await fetch(API_CONFIG.groq.endpoint, {
                method: 'POST',
                headers: {
                    'Authorization': `Bearer ${API_CONFIG.groq.key}`,
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    model: model,
                    messages: messages,
                    temperature: currentMode === 'nix' ? 0.5 : currentMode === 'nova' ? 0.9 : 0.7,
                    max_tokens: currentMode === 'nix' ? 512 : currentMode === 'nova' ? 2048 : 1024
                })
            });

            if (!response.ok) {
                const errorText = await response.text();
                let errorMessage = 'API request failed';
                
                try {
                    const errorData = JSON.parse(errorText);
                    errorMessage = errorData.error?.message || errorData.message || errorMessage;
                } catch (e) {
                    errorMessage = errorText;
                }
                
                if (response.status === 401) {
                    throw new Error('Invalid API key. Please check your Groq API key in settings.');
                } else if (response.status === 429) {
                    throw new Error('Rate limit exceeded. Please wait a moment and try again.');
                } else if (response.status === 500 || response.status === 502 || response.status === 503) {
                    throw new Error('Groq service is temporarily unavailable. Please try again in a moment.');
                } else {
                    throw new Error(`Groq API Error (${response.status}): ${errorMessage}`);
                }
            }

            const data = await response.json();
            return data.choices[0].message.content;
        }

        async function callAnthropicAPI(systemPrompt, history, userMessage) {
            const messages = [
                ...history,
                { role: 'user', content: userMessage }
            ];

            const response = await fetch(API_CONFIG.anthropic.endpoint, {
                method: 'POST',
                headers: {
                    'x-api-key': API_CONFIG.anthropic.key,
                    'anthropic-version': '2023-06-01',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    model: API_CONFIG.anthropic.model,
                    max_tokens: currentMode === 'nix' ? 512 : currentMode === 'nova' ? 2048 : 1024,
                    system: systemPrompt,
                    messages: messages
                })
            });

            if (!response.ok) {
                const errorText = await response.text();
                let errorMessage = 'Anthropic API request failed';
                
                try {
                    const errorData = JSON.parse(errorText);
                    errorMessage = errorData.error?.message || errorData.message || errorMessage;
                } catch (e) {
                    errorMessage = errorText;
                }
                
                throw new Error(errorMessage);
            }

            const data = await response.json();
            return data.content[0].text;
        }

        function handleKeyDown(event) {
            if (event.key === 'Enter' && !event.shiftKey) {
                event.preventDefault();
                sendMessage();
            }
        }

        function autoResizeInput(textarea) {
            textarea.style.height = 'auto';
            const newHeight = Math.min(textarea.scrollHeight, 96);
            textarea.style.height = newHeight + 'px';
            
            const wrapper = textarea.parentElement;
            wrapper.style.minHeight = '40px';
            wrapper.style.height = 'auto';
        }

        function setAIMode(mode) {
            const valid_modes = ["default", "nix", "nova"];
            if (!valid_modes.includes(mode)) return;
            
            currentMode = mode;
            
            const mode_names = {
                "default": "Cyanix",
                "nix": "Nix",
                "nova": "Nova"
            };
            
            addMessage(`AI mode: ${mode_names[mode]}`, false);
            if (autoSpeak && 'speechSynthesis' in window) {
                speak(`Mode switched to ${mode_names[mode].toLowerCase()}.`);
            }
            
            if (menuOpen) {
                toggleMenu();
            }
        }

        function toggleAutoSpeak() {
            autoSpeak = document.getElementById('autoSpeakToggle').checked;
        }

        function speak(text) {
            if (!autoSpeak || !('speechSynthesis' in window)) return;
            
            const utterance = new SpeechSynthesisUtterance(text);
            const speed = document.getElementById('voiceSpeedSlider').value / 100;
            utterance.rate = speed;
            speechSynthesis.speak(utterance);
        }

        function showAPIKeyDialog() {
            const dialog = document.getElementById('apiKeyDialog');
            dialog.classList.remove('hidden');
            
            const groqKey = localStorage.getItem('groq_api_key') || '';
            const anthropicKey = localStorage.getItem('anthropic_api_key') || '';
            
            document.getElementById('groqKeyInput').value = groqKey;
            document.getElementById('anthropicKeyInput').value = anthropicKey;
            
            updateAPIStatus();
            
            if (menuOpen) {
                toggleMenu();
            }
        }

        function closeAPIKeyDialog() {
            document.getElementById('apiKeyDialog').classList.add('hidden');
        }

        function saveAPIKeys() {
            const groqKey = document.getElementById('groqKeyInput').value.trim();
            const anthropicKey = document.getElementById('anthropicKeyInput').value.trim();
            
            if (groqKey) {
                localStorage.setItem('groq_api_key', groqKey);
                API_CONFIG.groq.key = groqKey;
            }
            
            if (anthropicKey) {
                localStorage.setItem('anthropic_api_key', anthropicKey);
                API_CONFIG.anthropic.key = anthropicKey;
            }
            
            updateAPIStatus();
            closeAPIKeyDialog();
            
            if (groqKey) {
                testAPIKey();
            } else {
                addMessage('API keys saved successfully!', false);
            }
        }

        async function testAPIKey() {
            addMessage('Testing API connection...', false);
            
            try {
                const response = await fetch(API_CONFIG.groq.endpoint, {
                    method: 'POST',
                    headers: {
                        'Authorization': `Bearer ${API_CONFIG.groq.key}`,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({
                        model: 'llama-3.1-8b-instant',
                        messages: [
                            { role: 'user', content: 'Hi' }
                        ],
                        max_tokens: 50
                    })
                });

                if (response.ok) {
                    addMessage('✅ API key is working! You can now chat with AI.', false);
                } else {
                    const errorText = await response.text();
                    let errorMsg = 'Unknown error';
                    try {
                        const errorData = JSON.parse(errorText);
                        errorMsg = errorData.error?.message || errorData.message || errorMsg;
                    } catch (e) {
                        errorMsg = errorText;
                    }
                    
                    if (response.status === 401) {
                        addMessage('❌ Invalid API key. Please check your key and try again. Get a key at console.groq.com', false);
                    } else {
                        addMessage(`❌ API Error (${response.status}): ${errorMsg}`, false);
                    }
                }
            } catch (error) {
                addMessage(`❌ Connection error: ${error.message}. Please check your internet connection.`, false);
            }
        }

        function updateAPIStatus() {
            const groqStatus = document.getElementById('groqStatus');
            const anthropicStatus = document.getElementById('anthropicStatus');
            
            if (API_CONFIG.groq.key) {
                groqStatus.textContent = 'Configured';
                groqStatus.className = 'api-status configured';
            } else {
                groqStatus.textContent = 'Not Configured';
                groqStatus.className = 'api-status not-configured';
            }
            
            if (API_CONFIG.anthropic.key) {
                anthropicStatus.textContent = 'Configured';
                anthropicStatus.className = 'api-status configured';
            } else {
                anthropicStatus.textContent = 'Not Configured';
                anthropicStatus.className = 'api-status not-configured';
            }
        }

        // Initialize
        document.addEventListener('DOMContentLoaded', function() {
            const loginInput = document.getElementById('apiKeyLoginInput');
            if (loginInput) {
                loginInput.addEventListener('keypress', function(e) {
                    if (e.key === 'Enter') login();
                });
            }
        });

        window.addEventListener('load', function() {
            const input = document.getElementById('messageInput');
            if (input) {
                input.style.height = 'auto';
                const wrapper = input.parentElement;
                if (wrapper) {
                    wrapper.style.minHeight = '40px';
                    wrapper.style.height = 'auto';
                }
            }
            
            if (/iPhone|iPad|iPod/.test(navigator.userAgent)) {
                const viewport = document.querySelector('meta[name=viewport]');
                if (viewport) {
                    viewport.setAttribute('content', 'width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no');
                }
            }
        });

        // ==================== PWA Service Worker Registration ====================
        if ('serviceWorker' in navigator) {
            window.addEventListener('load', function() {
                navigator.serviceWorker.register('/CyanixAi/sw.js')
                    .then(function(registration) {
                        console.log('✅ PWA Service Worker registered:', registration.scope);
                    })
                    .catch(function(error) {
                        console.log('❌ Service Worker failed:', error);
                    });
            });
        }
    </script>
</body>
</html>