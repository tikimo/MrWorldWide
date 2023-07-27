# MrWorldWide
7x7 Polydactyl Rex Build

Wiring diagram is available at the root of the repo

## Current issues

### Rewiring right side 
Right side has to be 7x7 instead of 6x7, in order to be identical to left side. I think this causes issues with `coord_mapping` to get confused. 
#### Produces:
Key 47 and 48 are treated as one key, idk why but this is assumed because of len(rows)*len(cols) doesnt match on both sides.

### UART communication
I cant make the two sides communicate with each other, idk why. I've tried multiple different setups. Power does go through, but RX/TX is not working.

In the wiring, I have TX/RX on GP0 and GP1 (Pi Pico W). 

Also, devices are named `MRWWL` and `MRWWR`.

#### Setups i've tried:
```python
split = Split(
    data_pin=board.GP1,
    debug_enabled=True,
)
```
```python
split = Split(
    split_side=SplitSide.RIGHT, # and left respectively
    split_type=SplitType.UART,
    split_target_left=False,
    data_pin=board.GP1,
    data_pin2=board.GP0,
    debug_enabled=True,
)
```
```python
split = Split(
    split_side=SplitSide.RIGHT,
    split_type=SplitType.UART,
    data_pin=board.GP0,
    data_pin2=board.GP1,
    debug_enabled=True,
)
```
```python
split = Split(
    split_side=SplitSide.RIGHT,
    split_type=SplitType.UART,
    data_pin=board.GP0,
    data_pin2=board.GP1,
    use_pio=True,
    debug_enabled=True,
)
```
