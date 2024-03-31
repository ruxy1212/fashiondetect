# app/__init__.py
from flask import Flask
from detectron2.data import DatasetCatalog, MetadataCatalog
from .routes import main_bp
from .filters import b64encode
from .utils import get_sign_dicts

def create_app():
    app = Flask(__name__)

    # Register your custom dataset during application initialization
    # for d in ["train", "val"]:
    #     DatasetCatalog.register("traffic_sign_" + d, lambda d=d: get_sign_dicts('./' + d))
    #     MetadataCatalog.get("traffic_sign_" + d).set(thing_classes=['prohibitory', 'danger', 'mandatory', 'other'])

    dataset_train = "dt_train"
    dataset_val = "dt_val"

    if dataset_train in DatasetCatalog.list():
        DatasetCatalog.remove(dataset_train)
    if dataset_val in DatasetCatalog.list():
        DatasetCatalog.remove(dataset_val)
    if dataset_train in MetadataCatalog.list():
        MetadataCatalog.remove(dataset_train)
    if dataset_val in MetadataCatalog.list():
        MetadataCatalog.remove(dataset_val)

    from detectron2.data.datasets import register_coco_instances
    register_coco_instances(dataset_train, {}, "/dataset/instances_attributes_train2020.json", "/dataset/train")
    register_coco_instances(dataset_val, {}, "/dataset/instances_attributes_val2020.json", "/dataset/test")

    # Register custom filters
    app.jinja_env.filters['b64encode'] = b64encode

    # Register blueprints
    app.register_blueprint(main_bp)

    return app


