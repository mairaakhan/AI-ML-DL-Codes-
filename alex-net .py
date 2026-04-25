#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
)
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau
import matplotlib.pyplot as plt


# In[32]:


# ==============================
# 1. Load CIFAR-10 Data
# ==============================
(X_train, y_train), (X_test, y_test) = cifar10.load_data()


# In[33]:


# ==============================
# 2. Preprocessing
# ==============================

# Normalize (VERY important for CIFAR)
X_train = X_train.astype("float32") / 255.0
X_test = X_test.astype("float32") / 255.0

# One-hot encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)


# In[34]:


# ==============================
# 3. AlexNet-style CNN (CIFAR adapted)
# ==============================
model = Sequential()


# In[35]:


# Block 1
model.add(Conv2D(64, (3,3), padding='same', activation='relu', input_shape=(32,32,3)))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))


# In[36]:


# Block 2
model.add(Conv2D(128, (3,3), padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))


# In[37]:


# Block 3
model.add(Conv2D(256, (3,3), padding='same', activation='relu'))
model.add(BatchNormalization())


# In[38]:


# Block 4
model.add(Conv2D(256, (3,3), padding='same', activation='relu'))
model.add(BatchNormalization())
model.add(MaxPooling2D(pool_size=(2,2)))


# In[39]:


# Flatten
model.add(Flatten())


# In[40]:


# Fully Connected layers
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))


# In[41]:


model.add(Dense(512, activation='relu'))
model.add(Dropout(0.5))


# In[42]:


# Output layer
model.add(Dense(10, activation='softmax'))


# In[43]:


# ==============================
# 4. Compile Model
# ==============================
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)


# In[44]:


# ==============================
# 5. Callbacks
# ==============================
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=5,
    restore_best_weights=True
)

lr_schedule = ReduceLROnPlateau(
    monitor='val_loss',
    factor=0.5,
    patience=3
)


# In[45]:


# ==============================
# 6. Train Model
# ==============================
history = model.fit(
    X_train, y_train,
    epochs=10,
    batch_size=64,
    validation_split=0.2,
    callbacks=[early_stop, lr_schedule]
)


# In[46]:


# ==============================
# 7. Evaluate
# ==============================
test_loss, test_acc = model.evaluate(X_test, y_test)
print("Test Accuracy:", test_acc)


# In[47]:


# ==============================
# 8. Plot Accuracy
# ==============================
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('CIFAR-10 Model Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend(['Train', 'Validation'])
plt.show()


# In[48]:


# ==============================
# 9. Plot Loss
# ==============================
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('CIFAR-10 Model Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend(['Train', 'Validation'])
plt.show()


# In[49]:


# ==============================
# 10. Predictions
# ==============================
y_pred = model.predict(X_test)
y_pred_classes = np.argmax(y_pred, axis=1)
y_true = np.argmax(y_test, axis=1)


# In[50]:


# ==============================
# 11. Visualize Predictions
# ==============================

class_names = ['airplane','automobile','bird','cat','deer',
               'dog','frog','horse','ship','truck']

plt.figure(figsize=(10,10))

for i in range(9):
    plt.subplot(3,3,i+1)
    plt.imshow(X_test[i])
    plt.title(f"Pred: {class_names[y_pred_classes[i]]}\nTrue: {class_names[y_true[i]]}")
    plt.axis('off')

plt.tight_layout()
plt.show()


# In[51]:


from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

cm = confusion_matrix(y_true, y_pred_classes)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=class_names)
disp.plot(cmap='Blues', xticks_rotation=45)
plt.title("Confusion Matrix")
plt.show()


# In[52]:


from sklearn.metrics import classification_report

print(classification_report(y_true, y_pred_classes, target_names=class_names))


# In[ ]:




