for dirpath, dirnames, filenames in os.walk("/kaggle/input/chest-xray-pneumonia/chest_xray"):
print(f"There are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")
train_dir = '/kaggle/input/chest-xray-pneumonia/chest_xray/train'
test_dir = '/kaggle/input/chest-xray-pneumonia/chest_xray/test'
val_dir = '/kaggle/input/chest-xray-pneumonia/chest_xray/chest_xray/val'
IMG_SIZE = (224,224)
BATCH_SIZE = 32

train_gen = ImageDataGenerator(
                rescale=1. / 255,
                horizontal_flip=True)
val_gen = ImageDataGenerator(rescale=1. / 255)
test_gen = ImageDataGenerator(rescale=1. / 255)
train_data= train_gen.flow_from_directory(
    train_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    shuffle = True)
val_data = val_gen.flow_from_directory(
    val_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary')
test_data = test_gen.flow_from_directory(
    test_dir,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary')
train_batch, train_batch_label = next(iter(train_data))
show_data(train_batch, train_batch_label,'Train Data')
val_batch, val_batch_label = next(iter(val_data))
show_data(val_batch, val_batch_label,'Validation Data')
test_batch, test_batch_label = next(iter(test_data))
show_data(test_batch, test_batch_label,'Test Data')
