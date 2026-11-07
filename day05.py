class Clock:
    id=None
    price=None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

clock=Clock()
clock.id="000320"
clock.price=21.99
print(f"闹钟的编号是{clock.id},闹钟的价格是{clock.price}")
clock.ring()