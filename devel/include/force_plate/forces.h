// Generated by gencpp from file force_plate/forces.msg
// DO NOT EDIT!


#ifndef FORCE_PLATE_MESSAGE_FORCES_H
#define FORCE_PLATE_MESSAGE_FORCES_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace force_plate
{
template <class ContainerAllocator>
struct forces_
{
  typedef forces_<ContainerAllocator> Type;

  forces_()
    : f1(0.0)
    , f2(0.0)
    , f3(0.0)
    , f4(0.0)  {
    }
  forces_(const ContainerAllocator& _alloc)
    : f1(0.0)
    , f2(0.0)
    , f3(0.0)
    , f4(0.0)  {
  (void)_alloc;
    }



   typedef float _f1_type;
  _f1_type f1;

   typedef float _f2_type;
  _f2_type f2;

   typedef float _f3_type;
  _f3_type f3;

   typedef float _f4_type;
  _f4_type f4;





  typedef boost::shared_ptr< ::force_plate::forces_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::force_plate::forces_<ContainerAllocator> const> ConstPtr;

}; // struct forces_

typedef ::force_plate::forces_<std::allocator<void> > forces;

typedef boost::shared_ptr< ::force_plate::forces > forcesPtr;
typedef boost::shared_ptr< ::force_plate::forces const> forcesConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::force_plate::forces_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::force_plate::forces_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::force_plate::forces_<ContainerAllocator1> & lhs, const ::force_plate::forces_<ContainerAllocator2> & rhs)
{
  return lhs.f1 == rhs.f1 &&
    lhs.f2 == rhs.f2 &&
    lhs.f3 == rhs.f3 &&
    lhs.f4 == rhs.f4;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::force_plate::forces_<ContainerAllocator1> & lhs, const ::force_plate::forces_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace force_plate

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::force_plate::forces_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::force_plate::forces_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::force_plate::forces_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::force_plate::forces_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::force_plate::forces_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::force_plate::forces_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::force_plate::forces_<ContainerAllocator> >
{
  static const char* value()
  {
    return "5c28bd9029eb1eda370389d9a92395b2";
  }

  static const char* value(const ::force_plate::forces_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x5c28bd9029eb1edaULL;
  static const uint64_t static_value2 = 0x370389d9a92395b2ULL;
};

template<class ContainerAllocator>
struct DataType< ::force_plate::forces_<ContainerAllocator> >
{
  static const char* value()
  {
    return "force_plate/forces";
  }

  static const char* value(const ::force_plate::forces_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::force_plate::forces_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float32 f1\n"
"float32 f2\n"
"float32 f3\n"
"float32 f4\n"
;
  }

  static const char* value(const ::force_plate::forces_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::force_plate::forces_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.f1);
      stream.next(m.f2);
      stream.next(m.f3);
      stream.next(m.f4);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct forces_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::force_plate::forces_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::force_plate::forces_<ContainerAllocator>& v)
  {
    s << indent << "f1: ";
    Printer<float>::stream(s, indent + "  ", v.f1);
    s << indent << "f2: ";
    Printer<float>::stream(s, indent + "  ", v.f2);
    s << indent << "f3: ";
    Printer<float>::stream(s, indent + "  ", v.f3);
    s << indent << "f4: ";
    Printer<float>::stream(s, indent + "  ", v.f4);
  }
};

} // namespace message_operations
} // namespace ros

#endif // FORCE_PLATE_MESSAGE_FORCES_H
