from boto import ec2
from django.db import models


class Instance(models.Model):
    """
    An EC2 instance.
    """

    ami_id = models.CharField(max_length=100)
    instance_type = models.CharField(max_length=100)
    availability_zone = models.CharField(max_length=100)
    access_key_id = models.CharField(max_length=100)
    secret_access_key = models.CharField(max_length=100)

    running = models.BooleanField(default=False)

    class Meta:
        ordering = ('ami_id',)

    def __unicode__(self):
        return u'{} / {} / {}'.format(self.ami_id, self.instance_type, self.availability_zone)

    def _show_instances(self):
        """
        Shows instances given the Access Key ID and Secret Access Key.
        """
        conn = ec2.connect_to_region(
            self.availability_zone,
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key,
        )
        reservations = conn.get_all_reservations()
        for reservation in reservations:
            print reservation
            for instance in reservation.instances:
                print instance
                print '- AMI ID:', instance.image_id
                print '- Instance Type:', instance.instance_type
                print '- Availability Zone:', instance.placement

    def launch(self):
        """
        Launches the instance if it's not running.
        """
        if self.running:
            return

        conn = ec2.connect_to_region(
            self.availability_zone,
            aws_access_key_id=self.access_key_id,
            aws_secret_access_key=self.secret_access_key,
        )
        conn.run_instances(self.ami_id, instance_type=self.instance_type)

        self.running = True
        self.save()
