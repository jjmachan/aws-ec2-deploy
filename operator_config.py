OPERATOR_NAME = "aws-ec2"

OPERATOR_MODULE = "bentoctl_aws_ec2"

OPERATOR_SCHEMA = {
    "region": {
        "required": True,
        "type": "string",
        "default": "us-west-1",
        "help_message": "AWS region to which you want to deploy",
    },
    "instance_type": {
        "type": "string",
        "default": "t2.macro",
        "help_message": "Instance type for the EC2 deployment."
        " See https://aws.amazon.com/ec2/instance-types/ for the entire list.",
    },
    "ami_id": {
        "type": "string",
        "default": "/aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2",
        "help_message": "Amazon Machine Image (AMI) used for the EC2 instance. "
        "Check out https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html "
        "for more information.",
    },
    "enable_gpus": {
        "type": "bool",
        "default": "False",
        "coercion": bool,
        "help_message": "If using GPU-accelerated instance_types then ennable this.",
    },
    "ec2_auto_scale": {
        "type": "dict",
        "schema": {
            "min_size": {
                "type": "int",
                "default": 1,
                "help_message": "The minimum number of instances for the auto "
                "scale group",
                "coercion": int,
            },
            "desired_capacity": {
                "type": "int",
                "default": 1,
                "coercion": int,
                "help_message": "The Auto Scaling Group will start with as many "
                "instances as specified by 'desired_capacity'.",
            },
            "max_size": {
                "type": "int",
                "default": 1,
                "coercion": int,
                "help_message": "The maximum number of instances for the autoscaling "
                "group",
            },
        },
    },
    "elastic_load_balancing": {
        "type": "dict",
        "schema": {
            "health_check_interval_seconds": {
                "type": "int",
                "default": 5,
                "coercion": int,
                "help_message": "Interval between health checks of instances in"
                " seconds.",
                'min': 5,
                'max': 300
            },
            'health_check_path': {
                'type': 'string',
                'default': '/healthz',
                "help_message": "The URL path for health check"
                },
            'health_check_port': {
                'type': 'string',
                'default': '5000',
                "coercion": int,
                'help_message': 'Health check port'
                },
            'health_check_timeout_seconds': {
                'type': 'int',
                'default': 3,
                'coercion': int,
                'help_message': 'Seconds to wait before health check times out'
                },
            'health_threshold_count': {
                'type': 'int',
                'default': 2,
                'coercion': int,
                'min': 2,
                'max': 10
                }
        },
    },
}
