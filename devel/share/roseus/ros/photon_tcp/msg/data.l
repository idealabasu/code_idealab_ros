;; Auto-generated. Do not edit!


(when (boundp 'photon_tcp::data)
  (if (not (find-package "PHOTON_TCP"))
    (make-package "PHOTON_TCP"))
  (shadow 'data (find-package "PHOTON_TCP")))
(unless (find-package "PHOTON_TCP::DATA")
  (make-package "PHOTON_TCP::DATA"))

(in-package "ROS")
;;//! \htmlinclude data.msg.html


(defclass photon_tcp::data
  :super ros::object
  :slots (_ip_address _data ))

(defmethod photon_tcp::data
  (:init
   (&key
    ((:ip_address __ip_address) "")
    ((:data __data) "")
    )
   (send-super :init)
   (setq _ip_address (string __ip_address))
   (setq _data (string __data))
   self)
  (:ip_address
   (&optional __ip_address)
   (if __ip_address (setq _ip_address __ip_address)) _ip_address)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; string _ip_address
    4 (length _ip_address)
    ;; string _data
    4 (length _data)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _ip_address
       (write-long (length _ip_address) s) (princ _ip_address s)
     ;; string _data
       (write-long (length _data) s) (princ _data s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _ip_address
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _ip_address (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; string _data
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _data (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get photon_tcp::data :md5sum-) "9c1f1555d04a791e7f80e64d4a99bed2")
(setf (get photon_tcp::data :datatype-) "photon_tcp/data")
(setf (get photon_tcp::data :definition-)
      "string ip_address
string data

")



(provide :photon_tcp/data "9c1f1555d04a791e7f80e64d4a99bed2")


