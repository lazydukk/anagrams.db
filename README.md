# anagrams.db

## Custom tile sets
- `1.1x` --> upscaled by 1.1 to avoid NASPA Zyzzyva's weird bug.
- to use them paste them into `data/tiles` folder in the installation directory.
	- ex: `C:\Program Files\NASPA Zyzzyva 3.4.1\data\tiles`

## Aerolith list to Zyzzyva
- run `./aerolith/scripty.py` then enter the file name;
- or just run the `aero-to-zyzzyva-windows.exe` (windows only)
- as an example: 4s-08-25.txt
- then import the `stripped-4s-08-25.txt` file in to zyzzyva.


## Cardbox 
`update questions SET next_scheduled = next_scheduled + 86400*12
    where next_scheduled is not null  and next_scheduled > strftime('%s','now') + 86400*12 
    AND next_scheduled % 2 =0`
(credits: (e4c5)[https://github.com/e4c5]
