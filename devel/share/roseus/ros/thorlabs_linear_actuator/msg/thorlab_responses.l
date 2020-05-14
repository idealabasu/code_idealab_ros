;; Auto-generated. Do not edit!


(when (boundp 'thorlabs_linear_actuator::thorlab_responses)
  (if (not (find-package "THORLABS_LINEAR_ACTUATOR"))
    (make-package "THORLABS_LINEAR_ACTUATOR"))
  (shadow 'thorlab_responses (find-package "THORLABS_LINEAR_ACTUATOR")))
(unless (find-package "THORLABS_LINEAR_ACTUATOR::THORLAB_RESPONSES")
  (make-package "THORLABS_LINEAR_ACTUATOR::THORLAB_RESPONSES"))

(in-package "ROS")
;;//! \htmlinclude thorlab_responses.msg.html


(defclass thorlabs_linear_actuator::thorlab_responses
  :super ros::object
  :slots (_response ))

(defmethod thorlabs_linear_actuator::thorlab_responses
  (:init
   (&key
    ((:response __response) "")
    )
   (send-super :init)
   (setq _response (string __response))
   self)
  (:response
   (&optional __response)
   (if __response (setq _response __response)) _response)
  (:serialization-length
   ()
   (+
    ;; string _response
    4 (length _response)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _response
       (write-long (length _response) s) (princ _response s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _response
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _response (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get thorlabs_linear_actuator::thorlab_responses :md5sum-) "6de314e2dc76fbff2b6244a6ad70b68d")
(setf (get thorlabs_linear_actuator::thorlab_responses :datatype-) "thorlabs_linear_actuator/thorlab_responses")
(setf (get thorlabs_linear_actuator::thorlab_responses :definition-)
      "string response
")



(provide :thorlabs_linear_actuator/thorlab_responses "6de314e2dc76fbff2b6244a6ad70b68d")


