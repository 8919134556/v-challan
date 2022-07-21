-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 21, 2022 at 08:55 AM
-- Server version: 10.4.21-MariaDB
-- PHP Version: 8.0.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `v_challana`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add vechile_ register', 7, 'add_vechile_register'),
(26, 'Can change vechile_ register', 7, 'change_vechile_register'),
(27, 'Can delete vechile_ register', 7, 'delete_vechile_register'),
(28, 'Can view vechile_ register', 7, 'view_vechile_register'),
(29, 'Can add fines', 8, 'add_fines'),
(30, 'Can change fines', 8, 'change_fines'),
(31, 'Can delete fines', 8, 'delete_fines'),
(32, 'Can view fines', 8, 'view_fines'),
(33, 'Can add v_ fines', 9, 'add_v_fines'),
(34, 'Can change v_ fines', 9, 'change_v_fines'),
(35, 'Can delete v_ fines', 9, 'delete_v_fines'),
(36, 'Can view v_ fines', 9, 'view_v_fines'),
(37, 'Can add payments', 10, 'add_payments'),
(38, 'Can change payments', 10, 'change_payments'),
(39, 'Can delete payments', 10, 'delete_payments'),
(40, 'Can view payments', 10, 'view_payments'),
(41, 'Can add complient', 11, 'add_complient'),
(42, 'Can change complient', 11, 'change_complient'),
(43, 'Can delete complient', 11, 'delete_complient'),
(44, 'Can view complient', 11, 'view_complient');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `complient`
--

CREATE TABLE `complient` (
  `id` int(11) NOT NULL,
  `tic_id` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `vechile_num` varchar(50) NOT NULL,
  `causes` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `complient` varchar(50) DEFAULT NULL,
  `datetime_created` datetime(6) NOT NULL,
  `user_email` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `complient`
--

INSERT INTO `complient` (`id`, `tic_id`, `user_name`, `vechile_num`, `causes`, `amount`, `complient`, `datetime_created`, `user_email`) VALUES
(4, '3135060857', 'suryaanand', 'LR33TEE', 'dunk and drive', '5000', 'it not me', '2022-07-20 15:47:49.271448', 'suryaanand456@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL CHECK (`action_flag` >= 0),
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(8, 'adminapp', 'fines'),
(7, 'adminapp', 'vechile_register'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(9, 'policeapp', 'v_fines'),
(6, 'sessions', 'session'),
(11, 'userapp', 'complient'),
(10, 'userapp', 'payments');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2022-07-07 06:13:55.596454'),
(2, 'auth', '0001_initial', '2022-07-07 06:13:57.458726'),
(3, 'admin', '0001_initial', '2022-07-07 06:13:57.846664'),
(4, 'admin', '0002_logentry_remove_auto_add', '2022-07-07 06:13:57.865615'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2022-07-07 06:13:57.885560'),
(6, 'contenttypes', '0002_remove_content_type_name', '2022-07-07 06:13:58.078719'),
(7, 'auth', '0002_alter_permission_name_max_length', '2022-07-07 06:13:58.219837'),
(8, 'auth', '0003_alter_user_email_max_length', '2022-07-07 06:13:58.253154'),
(9, 'auth', '0004_alter_user_username_opts', '2022-07-07 06:13:58.272108'),
(10, 'auth', '0005_alter_user_last_login_null', '2022-07-07 06:13:58.416164'),
(11, 'auth', '0006_require_contenttypes_0002', '2022-07-07 06:13:58.424270'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2022-07-07 06:13:58.451160'),
(13, 'auth', '0008_alter_user_username_max_length', '2022-07-07 06:13:58.488058'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2022-07-07 06:13:58.531942'),
(15, 'auth', '0010_alter_group_name_max_length', '2022-07-07 06:13:58.572884'),
(16, 'auth', '0011_update_proxy_permissions', '2022-07-07 06:13:58.593832'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2022-07-07 06:13:58.630729'),
(18, 'sessions', '0001_initial', '2022-07-07 06:13:58.777331'),
(19, 'adminapp', '0001_initial', '2022-07-12 12:30:29.553892'),
(20, 'adminapp', '0002_vechile_register_vechile_type', '2022-07-13 06:39:10.819029'),
(21, 'adminapp', '0003_fines', '2022-07-13 10:18:21.674673'),
(22, 'adminapp', '0004_auto_20220713_1606', '2022-07-13 10:36:33.095052'),
(23, 'adminapp', '0005_fines_image', '2022-07-13 12:05:13.303850'),
(24, 'adminapp', '0006_alter_fines_image', '2022-07-13 12:06:02.886136'),
(25, 'policeapp', '0001_initial', '2022-07-16 09:27:09.643865'),
(26, 'policeapp', '0002_auto_20220718_1434', '2022-07-18 09:04:13.791575'),
(27, 'policeapp', '0003_v_fines_user', '2022-07-18 09:21:46.829585'),
(28, 'userapp', '0001_initial', '2022-07-18 11:18:56.022510'),
(29, 'userapp', '0002_auto_20220719_1656', '2022-07-19 11:26:48.133197'),
(30, 'userapp', '0003_auto_20220720_1527', '2022-07-20 09:58:19.343857'),
(31, 'userapp', '0004_complient_user_email', '2022-07-20 10:16:43.473380');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('14u3ntfo3dl8mibsgjaoigubizndkihc', '.eJyrVirIz8lMTlWygjF0lEqLU4uAfDClo5Sam5iZA-QWlxZVJibmJealmJiaOaSDRPWS83OBKjJzE9NBBhjrFeSlA_kpiSWJQK6vh6e5U6CRpaURSCw1Nx9dLDNFycpCR6kgHsyoBQAI7il8:1oEQ2p:AqO9AQTGNsir9df2jNU6SnsmVXyzO74ADOo4rZQGifQ', '2022-08-04 06:52:23.815755');

-- --------------------------------------------------------

--
-- Table structure for table `fines`
--

CREATE TABLE `fines` (
  `id` int(11) NOT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `datetime_created` datetime(6) NOT NULL,
  `descrption` varchar(50) DEFAULT NULL,
  `prison` varchar(50) DEFAULT NULL,
  `title` varchar(50) DEFAULT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `fines`
--

INSERT INTO `fines` (`id`, `amount`, `datetime_created`, `descrption`, `prison`, `title`, `image`) VALUES
(2, '5000', '2022-07-13 16:32:45.787449', 'and/or 6 months in prison, Rs.15,000 and/or 2 year', '6 months', 'dunk and drive', 'admin/fine-image/drunk.jpg'),
(3, '1000', '2022-07-13 16:33:34.456664', 'plus licence scrapping for three months', 'three months', 'Riding without helmet', 'admin/fine-image/helmat_qGVjCIH.jpg'),
(4, '1000', '2022-07-13 16:34:05.616134', ' ₹ 5000/- and/or community service', 'none', 'Driving without licence', 'admin/fine-image/licences.jpg'),
(5, '1000', '2022-07-13 16:34:33.247401', 'for LMV, Rs.2,000 for MMV', 'none', 'Over speeding', 'admin/fine-image/over.jpg'),
(6, '1000', '2022-07-13 16:35:09.965094', '1000 to Rs.5,000, licence seizure, and/or 6 months', '6 months', 'Signal jumping', 'admin/fine-image/signals.jpg'),
(7, '25000', '2022-07-13 16:35:43.749673', '25000 with three years of imprisonment, cancellati', '1 year', 'Juvenile driving', 'admin/fine-image/44.jpg');

-- --------------------------------------------------------

--
-- Table structure for table `payments`
--

CREATE TABLE `payments` (
  `id` int(11) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `vechile_make` varchar(50) NOT NULL,
  `causes` varchar(50) DEFAULT NULL,
  `amount` varchar(50) DEFAULT NULL,
  `vechile_color` varchar(50) NOT NULL,
  `vechile_number` varchar(50) NOT NULL,
  `order_id` varchar(50) DEFAULT NULL,
  `status` varchar(50) DEFAULT NULL,
  `bank_name` varchar(50) DEFAULT NULL,
  `bank_tex_id` varchar(50) DEFAULT NULL,
  `datetime_created` datetime(6) NOT NULL,
  `payment_mode` varchar(50) DEFAULT NULL,
  `tex_id` bigint(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `payments`
--

INSERT INTO `payments` (`id`, `user_name`, `vechile_make`, `causes`, `amount`, `vechile_color`, `vechile_number`, `order_id`, `status`, `bank_name`, `bank_tex_id`, `datetime_created`, `payment_mode`, `tex_id`) VALUES
(15, 'suryaanand', 'ford', 'dunk and drive', '5000', 'blue', 'LR33TEE', 'qu05zipl', 'Success', 'Axis Bank', '777001207653353', '2022-07-19 17:48:05.587160', 'DC', 9223372036854775807),
(16, 'suryaanand', 'ktm', 'Riding without helmet', '1000', 'red', 'MHI7BQ2992', '2693x80z', 'Success', 'Axis Bank', '777001704159212', '2022-07-19 17:54:16.288254', 'DC', 9223372036854775807),
(17, 'suryaanand', 'ford', 'dunk and drive', '5000', 'blue', 'LR33TEE', '4b2fpt1z', NULL, NULL, NULL, '2022-07-19 17:57:54.622341', NULL, NULL),
(18, 'suryaanand', 'ford', 'dunk and drive', '5000', 'blue', 'LR33TEE', 'e7jnb6o3', NULL, NULL, NULL, '2022-07-19 17:59:09.921183', NULL, NULL),
(19, 'suryaanand', 'ford', 'dunk and drive', '5000', 'blue', 'LR33TEE', '4ttedlxw', 'Success', 'Axis Bank', '777001708240326', '2022-07-19 18:39:44.830414', 'DC', 9223372036854775807),
(20, 'suryaanand', 'ktm', 'Riding without helmet', '1000', 'red', 'MHI7BQ2992', 'zxpf08q2', NULL, NULL, NULL, '2022-07-21 11:59:12.885551', NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `vechile_register`
--

CREATE TABLE `vechile_register` (
  `id` int(11) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_lastname` varchar(50) NOT NULL,
  `user_email` varchar(100) DEFAULT NULL,
  `user_phone` bigint(20) NOT NULL,
  `vechile_year` varchar(50) NOT NULL,
  `vechile_make` varchar(50) NOT NULL,
  `vechile_model` varchar(50) NOT NULL,
  `vechile_color` varchar(50) NOT NULL,
  `vechile_mileage` varchar(50) NOT NULL,
  `vechile_number` varchar(50) NOT NULL,
  `country` varchar(50) DEFAULT NULL,
  `state` varchar(50) DEFAULT NULL,
  `city` varchar(50) DEFAULT NULL,
  `street_name` varchar(50) NOT NULL,
  `house_number` varchar(50) NOT NULL,
  `user_image` varchar(100) NOT NULL,
  `Vechile_image` varchar(100) NOT NULL,
  `datetime_created` datetime(6) NOT NULL,
  `vechile_type` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `vechile_register`
--

INSERT INTO `vechile_register` (`id`, `gender`, `user_name`, `user_lastname`, `user_email`, `user_phone`, `vechile_year`, `vechile_make`, `vechile_model`, `vechile_color`, `vechile_mileage`, `vechile_number`, `country`, `state`, `city`, `street_name`, `house_number`, `user_image`, `Vechile_image`, `datetime_created`, `vechile_type`) VALUES
(1, 'Male', 'suryaanand', 'nadendla', 'suryaanand456@gmail.com', 8919134556, '2018', 'ktm', 'c-120', 'red', '60', 'MHI7BQ2992', 'India', 'Andhra Pradesh', 'Guntur', 'bharath pet 2nd line', '4-16-55', 'User/Profile-image/2_XYR4Cwu.jpg', 'User/Vechile-image/7_XTtv4Wm.png', '2022-07-13 12:09:21.633916', 'Bike'),
(2, 'Male', 'suryaanand', 'nadendla', 'suryaanand456@gmail.com', 8919134556, '2012', 'ford', 'v-120', 'blue', '70', 'LR33TEE', 'India', 'Andhra Pradesh', 'Guntakai', 'adsfzdgrxhfj', 'qsdefs', 'User/Profile-image/2_EksegSb.jpg', 'User/Vechile-image/3.jpg', '2022-07-14 11:56:37.100878', 'Car'),
(3, 'Male', 'demo', 'demo', 'demo@gmail.com', 1234567890, '2012', 'suziki', 'demo-20', 'yellow', '60', 'AB52CD 5555', 'India', 'Andhra Pradesh', 'Guntur', 'bharath pet 2nd line', 'demo', 'User/Profile-image/angry-chili-pepper-cartoon-vector-23038452.jpg', 'User/Vechile-image/24.jpg', '2022-07-21 11:57:40.465462', 'Car');

-- --------------------------------------------------------

--
-- Table structure for table `v_fines`
--

CREATE TABLE `v_fines` (
  `id` int(11) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `user_lastname` varchar(50) NOT NULL,
  `vechile_year` varchar(50) NOT NULL,
  `vechile_make` varchar(50) NOT NULL,
  `vechile_color` varchar(50) NOT NULL,
  `vechile_number` varchar(50) NOT NULL,
  `vechile_type` varchar(50) DEFAULT NULL,
  `Vechile_image` varchar(100) NOT NULL,
  `datetime_created` datetime(6) NOT NULL,
  `causes` varchar(50) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `v_fines`
--

INSERT INTO `v_fines` (`id`, `user_name`, `user_lastname`, `vechile_year`, `vechile_make`, `vechile_color`, `vechile_number`, `vechile_type`, `Vechile_image`, `datetime_created`, `causes`, `user_id`) VALUES
(8, 'suryaanand', 'nadendla', '2018', 'ktm', 'red', 'MHI7BQ2992', 'Bike', 'User/fins/3_sYsDLqa.png', '2022-07-18 14:52:13.704251', 'Riding without helmet', 3),
(9, 'suryaanand', 'nadendla', '2012', 'ford', 'blue', 'LR33TEE', 'Car', 'User/fins/3_bRBcLLi.jpg', '2022-07-18 15:06:58.223884', 'dunk and drive', 2),
(10, 'suryaanand', 'nadendla', '2012', 'ford', 'blue', 'LR33TEE', 'Car', 'User/fins/3_3M6NNGe.jpg', '2022-07-19 18:38:08.312620', 'Driving without licence', 4),
(11, 'suryaanand', 'nadendla', '2018', 'ktm', 'red', 'MHI7BQ2992', 'Bike', 'User/fins/3_fxIu24K.png', '2022-07-21 12:02:26.152877', 'Over speeding', 5);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `complient`
--
ALTER TABLE `complient`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `fines`
--
ALTER TABLE `fines`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `payments`
--
ALTER TABLE `payments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `vechile_register`
--
ALTER TABLE `vechile_register`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `v_fines`
--
ALTER TABLE `v_fines`
  ADD PRIMARY KEY (`id`),
  ADD KEY `V_Fines_user_id_00d4fddd_fk_Fines_id` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=45;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `complient`
--
ALTER TABLE `complient`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT for table `fines`
--
ALTER TABLE `fines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `payments`
--
ALTER TABLE `payments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `vechile_register`
--
ALTER TABLE `vechile_register`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `v_fines`
--
ALTER TABLE `v_fines`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `v_fines`
--
ALTER TABLE `v_fines`
  ADD CONSTRAINT `V_Fines_user_id_00d4fddd_fk_Fines_id` FOREIGN KEY (`user_id`) REFERENCES `fines` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
