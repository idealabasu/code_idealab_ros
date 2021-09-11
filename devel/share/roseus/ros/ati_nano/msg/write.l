;; Auto-generated. Do not edit!


(when (boundp 'ati_nano::write)
  (if (not (find-package "ATI_NANO"))
    (make-package "ATI_NANO"))
  (shadow 'write (find-package "ATI_NANO")))
(unless (find-package "ATI_NANO::WRITE")
  (make-package "ATI_NANO::WRITE"))

(in-package "ROS")
;;//! \htmlinclude write.msg.html


(defclass ati_nano::write
  :super ros::object
  :slots (_fx _fy _fz _tx _ty _tz ))

(defmethod ati_nano::write
  (:init
   (&key
    ((:fx __fx) 0.0)
    ((:fy __fy) 0.0)
    ((:fz __fz) 0.0)
    ((:tx __tx) 0.0)
    ((:ty __ty) 0.0)
    ((:tz __tz) 0.0)
    )
   (send-super :init)
   (setq _fx (float __fx))
   (setq _fy (float __fy))
   (setq _fz (float __fz))
   (setq _tx (float __tx))
   (setq _ty (float __ty))
   (setq _tz (float __tz))
   self)
  (:fx
   (&optional __fx)
   (if __fx (setq _fx __fx)) _fx)
  (:fy
   (&optional __fy)
   (if __fy (setq _fy __fy)) _fy)
  (:fz
   (&optional __fz)
   (if __fz (setq _fz __fz)) _fz)
  (:tx
   (&optional __tx)
   (if __tx (setq _tx __tx)) _tx)
  (:ty
   (&optional __ty)
   (if __ty (setq _ty __ty)) _ty)
  (:tz
   (&optional __tz)
   (if __tz (setq _tz __tz)) _tz)
  (:serialization-length
   ()
   (+
    ;; float32 _fx
    4
    ;; float32 _fy
    4
    ;; float32 _fz
    4
    ;; float32 _tx
    4
    ;; float32 _ty
    4
    ;; float32 _tz
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float32 _fx
       (sys::poke _fx (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _fy
       (sys::poke _fy (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _fz
       (sys::poke _fz (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _tx
       (sys::poke _tx (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _ty
       (sys::poke _ty (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _tz
       (sys::poke _tz (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float32 _fx
     (setq _fx (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _fy
     (setq _fy (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _fz
     (setq _fz (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _tx
     (setq _tx (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _ty
     (setq _ty (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _tz
     (setq _tz (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get ati_nano::write :md5sum-) "525bd7f46f455baf22b587d94f926977")
(setf (get ati_nano::write :datatype-) "ati_nano/write")
(setf (get ati_nano::write :definition-)
      "float32 fx
float32 fy
float32 fz
float32 tx
float32 ty
float32 tz

")



(provide :ati_nano/write "525bd7f46f455baf22b587d94f926977")


