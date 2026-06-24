from irremote import get_ir_device

dev = get_ir_device()
 
while(True):
    event = dev.read_one()
    if not event:
        continue
    elif event.value == 0x18:
        print("fwd")
    elif event.value == 0x52:
        print("bwd")
    elif event.value == 0x08:
        print("left")
    elif event.value == 0x5a:
        print("right")
    elif event.value == 0x0d:
        print("exiting gracefully...")
        break