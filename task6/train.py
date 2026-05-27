import tensorflow as tf
from tensorflow.keras import datasets, layers, models

def train_model():
    print("--- Loading CIFAR-10 Dataset ---")
    (train_images, train_labels), (test_images, test_labels) = datasets.cifar10.load_data()
    train_images, test_images = train_images / 255.0, test_images / 255.0

    print("--- Building CNN Model ---")
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(10, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

    print("--- Training for 3 Epochs ---")
    model.fit(train_images, train_labels, epochs=3, validation_data=(test_images, test_labels))

    model.save('cnn_model.h5')
    print("--- Successfully saved as 'cnn_model.h5' ---")

if __name__ == "__main__":
    train_model()