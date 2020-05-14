;; Auto-generated. Do not edit!


(when (boundp 'thorlabs_linear_actuator::write)
  (if (not (find-package "THORLABS_LINEAR_ACTUATOR"))
    (make-package "THORLABS_LINEAR_ACTUATOR"))
  (shadow 'write (find-package "THORLABS_LINEAR_ACTUATOR")))
(unless (find-package "THORLABS_LINEAR_ACTUATOR::WRITE")
  (make-package "THORLABS_LINEAR_ACTUATOR::WRITE"))

(in-package "ROS")
;;//! \htmlinclude write.msg.html


(defclass thorlabs_linear_actuator::write
  :super ros::object
  :slots (_register _value ))

(defmethod thorlabs_linear_actuator::write
  (:init
   (&key
    ((:register __register) 0)
    ((:value __value) 0)
    )
   (send-super :init)
   (setq _register (round __register))
   (setq _value (round __value))
   self)
  (:register
   (&optional __register)
   (if __register (setq _register __register)) _register)
  (:value
   (&optional __value)
   (if __value (setq _value __value)) _value)
  (:serialization-length
   ()
   (+
    ;; uint8 _register
    1
    ;; uint8 _value
    1
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint8 _register
       (write-byte _register s)
     ;; uint8 _value
       (write-byte _value s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint8 _register
     (setq _register (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;; uint8 _value
     (setq _value (sys::peek buf ptr- :char)) (incf ptr- 1)
   ;;
   self)
  )

(setf (get thorlabs_linear_actuator::write :md5sum-) "42a1ebb3a1d2bdfda4b28ad577afa942")
(setf (get thorlabs_linear_actuator::write :datatype-) "thorlabs_linear_actuator/write")
(setf (get thorlabs_linear_actuator::write :definition-)
      "uint8 register
uint8 value


")



(provide :thorlabs_linear_actuator/write "42a1ebb3a1d2bdfda4b28ad577afa942")


