/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50723
 Source Host           : localhost:3306
 Source Schema         : qunar

 Target Server Type    : MySQL
 Target Server Version : 50723
 File Encoding         : 65001

 Date: 21/09/2019 22:08:40
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for cate_comment
-- ----------------------------
DROP TABLE IF EXISTS `cate_comment`;
CREATE TABLE `cate_comment`  (
  `cate_number` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `star` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `comment` blob NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for cate_information
-- ----------------------------
DROP TABLE IF EXISTS `cate_information`;
CREATE TABLE `cate_information`  (
  `city_number` int(4) NOT NULL,
  `cate_name` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cate_number` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `star` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `rank` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pay` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `address` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `recommendation` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`cate_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for cate_words
-- ----------------------------
DROP TABLE IF EXISTS `cate_words`;
CREATE TABLE `cate_words`  (
  `cate_number` varchar(12) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `word` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for city_table
-- ----------------------------
DROP TABLE IF EXISTS `city_table`;
CREATE TABLE `city_table`  (
  `city_number` int(4) NOT NULL AUTO_INCREMENT,
  `city_name` varchar(25) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `city_website` varchar(60) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  PRIMARY KEY (`city_number`) USING BTREE,
  UNIQUE INDEX `city_name`(`city_name`) USING BTREE,
  UNIQUE INDEX `city_website`(`city_website`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 751 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hotel_comment
-- ----------------------------
DROP TABLE IF EXISTS `hotel_comment`;
CREATE TABLE `hotel_comment`  (
  `hotel_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `username` varchar(25) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `star` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `comment` blob NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hotel_info
-- ----------------------------
DROP TABLE IF EXISTS `hotel_info`;
CREATE TABLE `hotel_info`  (
  `city_number` int(4) NOT NULL,
  `hotel_name` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `hotel_number` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `hotelType` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `rank` int(6) NOT NULL,
  `star` varchar(4) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `lat` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `lng` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  PRIMARY KEY (`hotel_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hotel_information
-- ----------------------------
DROP TABLE IF EXISTS `hotel_information`;
CREATE TABLE `hotel_information`  (
  `city_number` int(4) NOT NULL,
  `hotel_name` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hotel_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hotelType` varchar(16) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `rank` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `star` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `recommend` varchar(6) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `phoneConnect` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `introduction` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `hotelTime` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `childReductions` varchar(200) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `extraCharge` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `attention` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `otherService` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`hotel_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hotel_room
-- ----------------------------
DROP TABLE IF EXISTS `hotel_room`;
CREATE TABLE `hotel_room`  (
  `hotel_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `roomIntro` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `roomNumber` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `roomType` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `typeNumber` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hotel_roomprice
-- ----------------------------
DROP TABLE IF EXISTS `hotel_roomprice`;
CREATE TABLE `hotel_roomprice`  (
  `typeNumber` varchar(30) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `bedMessage` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `breakfast` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `rule` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `price` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hotel_words
-- ----------------------------
DROP TABLE IF EXISTS `hotel_words`;
CREATE TABLE `hotel_words`  (
  `hotel_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `word` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for newwords
-- ----------------------------
DROP TABLE IF EXISTS `newwords`;
CREATE TABLE `newwords`  (
  `scenery_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `word` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for scenery_comment
-- ----------------------------
DROP TABLE IF EXISTS `scenery_comment`;
CREATE TABLE `scenery_comment`  (
  `scenery_number` varchar(12) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `username` varchar(25) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `comment` blob NOT NULL,
  `star` varchar(4) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `suggestion` blob NOT NULL,
  `commentTime` varchar(14) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for scenery_strategy
-- ----------------------------
DROP TABLE IF EXISTS `scenery_strategy`;
CREATE TABLE `scenery_strategy`  (
  `strategy_number` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `playTime` varchar(5) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `cost` varchar(10) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `theme` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`strategy_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for scenery_table
-- ----------------------------
DROP TABLE IF EXISTS `scenery_table`;
CREATE TABLE `scenery_table`  (
  `city_number` varchar(4) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `scenery_number` varchar(12) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `scenery_name` varchar(60) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `ranking` varchar(8) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `grade` varchar(13) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `intro` varchar(100) CHARACTER SET gbk COLLATE gbk_chinese_ci NOT NULL,
  `suggest_time` varchar(20) CHARACTER SET gbk COLLATE gbk_chinese_ci DEFAULT NULL,
  `longitude` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  `latitude` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci DEFAULT NULL,
  PRIMARY KEY (`scenery_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for scenery_weight
-- ----------------------------
DROP TABLE IF EXISTS `scenery_weight`;
CREATE TABLE `scenery_weight`  (
  `scenery_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `weight` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`scenery_number`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for scenery_words
-- ----------------------------
DROP TABLE IF EXISTS `scenery_words`;
CREATE TABLE `scenery_words`  (
  `scenery_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `word` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for strategy_content
-- ----------------------------
DROP TABLE IF EXISTS `strategy_content`;
CREATE TABLE `strategy_content`  (
  `strategy_number` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `title` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `content` blob NOT NULL,
  `other` varchar(60) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for strategy_scenery
-- ----------------------------
DROP TABLE IF EXISTS `strategy_scenery`;
CREATE TABLE `strategy_scenery`  (
  `strategy_number` varchar(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `scenery_name` varchar(60) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
