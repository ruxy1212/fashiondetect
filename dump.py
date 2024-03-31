python -m detectron2.modeling.model_converters.convert_tf_checkpoint_to_pytorch \
    --tf_checkpoint_path /path/to/your/tf_checkpoint.ckpt \
    --output_path /path/to/save/pytorch_checkpoint.pth


import cv2
img_path = r"path/to/image"

#saving image into a white bg
img = cv2.imread(img_path, cv2.IMREAD_UNCHANGED)
b,g,r, a = cv2.split(img)
new_img  = cv2.merge((b, g, r))
not_a = cv2.bitwise_not(a)
not_a = cv2.cvtColor(not_a, cv2.COLOR_GRAY2BGR)
new_img = cv2.bitwise_and(new_img,new_img,mask = a)
new_img = cv2.add(new_img, not_a)
cv2.imwrite(output_dir, new_img)
print(new_img.shape)
cv2.imwrite(dir_img + id, img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])

with tf.Session() as sess:
    saver = tf.train.import_meta_graph('/tmp/model.ckpt.meta')
    saver.restore(sess, "/tmp/model.ckpt")
    save()