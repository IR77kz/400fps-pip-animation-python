from modules.ggg import generate
import time
import colorama
import datetime

colorama.init()
colorama.just_fix_windows_console()

index = 1

max_index = 45
min_index = 20

reached_max = False

colors = [
    colorama.Fore.MAGENTA,
]

try:
    s_fps = 0
    e_fps = 0
    fps = 0
    while True:
        s_fps = time.time()
        if index >= max_index and not reached_max:
            reached_max = True
        elif reached_max and index <= min_index:
            reached_max = False
        
        if reached_max:
            index=index-0.5
            time.sleep(0.01+(index/36000))
        else:
            index+=1
            time.sleep(0.01+(index/36000))
        print(f"""
{colorama.Back.GREEN}{colorama.Fore.RED}Date: {datetime.datetime.now()}{colorama.Fore.RESET}{colorama.Back.RESET}
{colorama.Back.GREEN}{colorama.Fore.RED}FPS: {int(fps)}{colorama.Fore.RESET}{colorama.Back.RESET}
{colorama.Back.MAGENTA}
{colorama.Fore.LIGHTGREEN_EX}
{generate(int(index/4), int(index*2), 1)}
{generate(int(index/3), int(index*2), 1)}
{generate(int(index/2.5), int(index*2), 1)}
{generate(int(index/2.7), int(index*2), 1)}
{generate(int(index/3), int(index), 1)}
{generate(int(index*1.16), int(index), 1)}
{generate(int(index*1.2), int(index), 1)}
{generate(int(index*1.2), int(index), 1)}
{generate(int(index*1.2), int(index), 1)}
{generate(int(index*1.16), int(index), 1)}
{generate(int(index/3), int(index), 1)}
{generate(int(index/2.7), int(index*2), 1)}
{generate(int(index/2.5), int(index*2), 1)}
{generate(int(index/3), int(index*2), 1)}
{generate(int(index/4), int(index*2), 1)}
{colorama.Fore.RESET}
{colorama.Back.RESET}
{colorama.Back.RED}{colorama.Fore.GREEN}INDEX: {index}{colorama.Fore.RESET}{colorama.Back.RESET}
""")
        e_fps = time.time()
        fps = int((e_fps - s_fps) * 36000)
        print("\033[H\033[J", end="")
except KeyboardInterrupt:
    pass
