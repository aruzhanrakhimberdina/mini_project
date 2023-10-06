import matplotlib.pyplot as plt
import pit

data = {
        "x" : [i for i in range(1, 10)],
        "y" : [i * i for i in range (1, 10)]
        }
pit.plot(
        data["x"],data["y"],
        )
plt. show()