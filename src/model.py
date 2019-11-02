# import tensorflow as tf
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras import Model
from tensorflow.keras.applications.resnet50 import ResNet50


class BruiseDetector():
    def __init__(self):
        super(BruiseDetector, self).__init__()
        resnet = ResNet50(weights='imagenet', input_shape=(300, 300, 3),
                          include_top=False, classes=2)
        x = resnet.output
        x = Flatten()(x)
        x = Dense(1024, activation='relu')(x)
        x = Dense(2, activation='softmax')(x)

        self.model = Model(resnet.input, x)

        self.model.compile(optimizer='adam',
                           loss='binary_crossentropy',
                           metrics=['accuracy'])

    def fit(self, x_train, y_train, batch=5, epochs=100):
        return self.model.fit(x_train, y_train,
                              batch=batch, epochs=epochs)

    def predict(self, x):
        return self.model.predict(x)

    def summary(self):
        return self.model.summary()


if __name__ == "__main__":
    model = BruiseDetector()

    model.summary()