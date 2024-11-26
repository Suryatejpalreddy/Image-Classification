for img_path in folder_dir.glob("*.jpg"):
        # Now we got directory/path of all jpg files in folders
        img = load_img(img_path,target_size=(32,32))
        img_array = img_to_array(img)
        image_data.append(img_array)
        labels.append(labels_dict[label])