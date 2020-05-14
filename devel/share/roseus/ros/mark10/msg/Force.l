;; Auto-generated. Do not edit!


(when (boundp 'mark10::Force)
  (if (not (find-package "MARK10"))
    (make-package "MARK10"))
  (shadow 'Force (find-package "MARK10")))
(unless (find-package "MARK10::FORCE")
  (make-package "MARK10::FORCE"))

(in-package "ROS")
;;//! \htmlinclude Force.msg.html


(defclass mark10::Force
  :super ros::object
  :slots (_force _unit ))

(defmethod mark10::Force
  (:init
   (&key
    ((:force __force) 0.0)
    ((:unit __unit) "")
    )
   (send-super :init)
   (setq _force (float __force))
   (setq _unit (string __unit))
   self)
  (:force
   (&optional __force)
   (if __force (setq _force __force)) _force)
  (:unit
   (&optional __unit)
   (if __unit (setq _unit __unit)) _unit)
  (:serialization-length
   ()
   (+
    ;; float32 _force
    4
    ;; string _unit
    4 (length _unit)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _force
       (sys::poke _force (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; string _unit
       (write-long (length _unit) s) (princ _unit s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _force
     (setq _force (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; string _unit
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _unit (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(setf (get mark10::Force :md5sum-) "ef3c99a919c971d6e0f206376229102e")
(setf (get mark10::Force :datatype-) "mark10/Force")
(setf (get mark10::Force :definition-)
      "float32 force
string unit

")



(provide :mark10/Force "ef3c99a919c971d6e0f206376229102e")


