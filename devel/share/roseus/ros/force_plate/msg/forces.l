;; Auto-generated. Do not edit!


(when (boundp 'force_plate::forces)
  (if (not (find-package "FORCE_PLATE"))
    (make-package "FORCE_PLATE"))
  (shadow 'forces (find-package "FORCE_PLATE")))
(unless (find-package "FORCE_PLATE::FORCES")
  (make-package "FORCE_PLATE::FORCES"))

(in-package "ROS")
;;//! \htmlinclude forces.msg.html


(defclass force_plate::forces
  :super ros::object
  :slots (_f1 _f2 _f3 _f4 ))

(defmethod force_plate::forces
  (:init
   (&key
    ((:f1 __f1) 0.0)
    ((:f2 __f2) 0.0)
    ((:f3 __f3) 0.0)
    ((:f4 __f4) 0.0)
    )
   (send-super :init)
   (setq _f1 (float __f1))
   (setq _f2 (float __f2))
   (setq _f3 (float __f3))
   (setq _f4 (float __f4))
   self)
  (:f1
   (&optional __f1)
   (if __f1 (setq _f1 __f1)) _f1)
  (:f2
   (&optional __f2)
   (if __f2 (setq _f2 __f2)) _f2)
  (:f3
   (&optional __f3)
   (if __f3 (setq _f3 __f3)) _f3)
  (:f4
   (&optional __f4)
   (if __f4 (setq _f4 __f4)) _f4)
  (:serialization-length
   ()
   (+
    ;; float32 _f1
    4
    ;; float32 _f2
    4
    ;; float32 _f3
    4
    ;; float32 _f4
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _f1
       (sys::poke _f1 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _f2
       (sys::poke _f2 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _f3
       (sys::poke _f3 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _f4
       (sys::poke _f4 (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _f1
     (setq _f1 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _f2
     (setq _f2 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _f3
     (setq _f3 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _f4
     (setq _f4 (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get force_plate::forces :md5sum-) "5c28bd9029eb1eda370389d9a92395b2")
(setf (get force_plate::forces :datatype-) "force_plate/forces")
(setf (get force_plate::forces :definition-)
      "float32 f1
float32 f2
float32 f3
float32 f4

")



(provide :force_plate/forces "5c28bd9029eb1eda370389d9a92395b2")


