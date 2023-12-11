for dirpath, dirnames, filenames in os.walk("/kaggle/input/chest-xray-pneumonia/chest_xray"):
  print(f"There are {len(dirnames)} directories and {len(filenames)} images in '{dirpath}'.")
