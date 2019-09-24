# Classification of MRI Scans
 
 **Class project made by Sagar Vakkala, RA1611003040145.**

 This deep learning model uses transfer learning on the VGG16 model (Which is initialised on the Imagenet weights).
 Two dropout layers, 1 Flatten layer and the trainable sigmoidal dense layer has been put in the end for the training.


 The trace log is:

 ```
 E:\Github projects\Classification-of-MRI-Scans> python .\train.py
Using TensorFlow backend.
Found 216 images belonging to 2 classes.
Found 18 images belonging to 2 classes.
2019-09-24 08:44:07.671593: I T:\src\github\tensorflow\tensorflow\core\platform\cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2
2019-09-24 08:44:07.981173: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:1392] Found device 0 with properties:
name: GeForce GTX 1080 major: 6 minor: 1 memoryClockRate(GHz): 1.7715
pciBusID: 0000:26:00.0
totalMemory: 8.00GiB freeMemory: 6.60GiB
2019-09-24 08:44:07.988576: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:1471] Adding visible gpu devices: 0
2019-09-24 08:44:12.364509: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:952] Device interconnect StreamExecutor with strength 1 edge matrix:
2019-09-24 08:44:12.368605: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:958]      0
2019-09-24 08:44:12.371299: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:971] 0:   N
2019-09-24 08:44:12.374915: I T:\src\github\tensorflow\tensorflow\core\common_runtime\gpu\gpu_device.cc:1084] Created TensorFlow device (/job:localhost/replica:0/task:0/device:GPU:0 with 6374 MB memory) -> physical GPU (device: 0, name: GeForce GTX 1080, pci bus id: 0000:26:00.0, compute capability: 6.1)
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
vgg16 (Model)                (None, 7, 7, 512)         14714688
_________________________________________________________________
dropout_1 (Dropout)          (None, 7, 7, 512)         0
_________________________________________________________________
flatten_1 (Flatten)          (None, 25088)             0
_________________________________________________________________
dropout_2 (Dropout)          (None, 25088)             0
_________________________________________________________________
dense_1 (Dense)              (None, 1)                 25089
=================================================================
Total params: 14,739,777
Trainable params: 25,089
Non-trainable params: 14,714,688
_________________________________________________________________
Epoch 1/120
50/50 [==============================] - 26s 524ms/step - loss: 3.1889 - acc: 0.6523 - val_loss: 1.3744 - val_acc: 0.8333
Epoch 2/120
50/50 [==============================] - 20s 402ms/step - loss: 1.7422 - acc: 0.8033 - val_loss: 0.5664 - val_acc: 0.8889
Epoch 3/120
50/50 [==============================] - 20s 404ms/step - loss: 1.3608 - acc: 0.8440 - val_loss: 0.5221 - val_acc: 0.9444

```
