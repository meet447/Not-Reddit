import asyncio
import json
import sys

try:
    import websockets
except ImportError:
    print("Websockets package not found. Make sure it's installed.")

# For local streaming, the websockets are hosted without ssl - ws://
HOST = 'wss://concerned-spread-customers-laptop.trycloudflare.com/api/v1/stream'
URI = f'{HOST}'

# For reverse-proxied streaming, the remote will likely host with ssl - wss://
# URI = 'wss://your-uri-here.trycloudflare.com/api/v1/stream'


async def run(user_input, history):
    # Note: the selected defaults change from time to time.
    request = {
        'prompt': "Draw a picture of a guy",

        'max_new_tokens': 250,
        'history': history,
        'mode': 'Chat',  # Valid options: 'chat', 'chat-instruct', 'instruct'
        'character': 'example',
        'instruction_template': 'waifu-workshop_Pygmalion-6b_orignal',
        'your_name': 'YOU',

        'regenerate': False,
        '_continue': False,
        'stop_at_newline': False,
        'chat_generation_attempts': 1,
        'chat-instruct_command': 'Continue the chat dialogue below. Write a single reply for the character "".\n\n',

        # Generation params. If 'preset' is set to different than 'None', the values
        # in presets/preset-name.yaml are used instead of the individual numbers.
        'preset': 'None',  
        'do_sample': True,
        'temperature': 0.7,
        'top_p': 0.1,
        'typical_p': 1,
        'epsilon_cutoff': 0,  # In units of 1e-4
        'eta_cutoff': 0,  # In units of 1e-4
        'tfs': 1,
        'top_a': 0,
        'repetition_penalty': 1.18,
        'repetition_penalty_range': 0,
        'top_k': 40,
        'min_length': 0,
        'no_repeat_ngram_size': 0,
        'num_beams': 1,
        'penalty_alpha': 0,
        'length_penalty': 1,
        'early_stopping': False,
        'mirostat_mode': 0,
        'mirostat_tau': 5,
        'mirostat_eta': 0.1,

        'seed': -1,
        'add_bos_token': True,
        'truncation_length': 2048,
        'ban_eos_token': False,
        'skip_special_tokens': True,
        'stopping_strings': []
    }

    async with websockets.connect(URI, ping_interval=None) as websocket:
        await websocket.send(json.dumps(request))

        while True:
            incoming_data = await websocket.recv()
            incoming_data = json.loads(incoming_data)
            if incoming_data['event'] == 'text_stream':
                print(incoming_data['text'], end='', flush=True)
            elif incoming_data['event'] == 'stream_end':
                return


if __name__ == '__main__':
    user_input = "ok?."

    # Basic example
    history = {'internal': [], 'visible': []}

    asyncio.run(run(user_input, history))
