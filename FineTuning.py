base_model.trainable = True
for layer in model.layers[1].layers[:-5]:
    layer.trainable = False
model.compile(loss=tf.keras.losses.binary_crossentropy,
              optimizer=tf.keras.optimizers.Adam(lr=0.00001),
              metrics=["binary_accuracy"])
checkpoint_path = "model_checkpoints/cp_fine_tunning.ckpt" 
model_checkpoint = tf.keras.callbacks.ModelCheckpoint(checkpoint_path,
                                                      monitor="val_accuracy",
                                                      save_best_only=True,
                                                      save_weights_only=True, 
                                                      verbose=0)
history_fine_tune = model.fit(train_data,
                            epochs=40,
                            validation_data=test_data,
                            initial_epoch=history.epoch[-1],
                            callbacks=[model_checkpoint,early_stopping])
